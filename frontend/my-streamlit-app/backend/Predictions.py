import os
import sys
import importlib
import streamlit as st
import contextlib
import numpy as np
import joblib
import alpaca_trade_api as tradeapi
import pandas as pd
from datetime import datetime, timezone, timedelta
import plotly.express as px
import requests

# Redirect all stderr to null to suppress C++ and Absl logs before TF import
devnull = os.open(os.devnull, os.O_WRONLY)
os.dup2(devnull, sys.stderr.fileno())
os.close(devnull)
# Environment to disable GPU and reduce TF logs
os.environ["CUDA_VISIBLE_DEVICES"] = ""
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
os.environ["TF_CPP_MIN_VLOG_LEVEL"] = "3"
os.environ["ABSL_CPP_MIN_LOG_LEVEL"] = "3"

# Suppress absl preinit warning before any absl or TF import
importlib.import_module("absl.logging")._warn_preinit_stderr = False


# Redirect any stderr from TensorFlow import into the void
def _import_tf():
    with open(os.devnull, "w") as _err_file, contextlib.redirect_stderr(_err_file):
        import tensorflow as tf
    return tf

# Load TensorFlow
tf = _import_tf()

# Cache model loading to prevent repeated retracing
@st.cache_resource
def _load_model(path):
    model = tf.keras.models.load_model(path)
    model.make_predict_function()
    return model

def get_stocks_ID(selected_stock):
    if selected_stock == "NVIDIA":
        selected_stock_ID = "NVDA"
    elif selected_stock == "APPLE":
        selected_stock_ID = "AAPL"
    elif selected_stock == "MICROSOFT":
        selected_stock_ID = "MSFT"
    elif selected_stock == "AMAZON":
        selected_stock_ID = "AMZN"
    elif selected_stock == "GOOGLE":
        selected_stock_ID = "GOOG"
    elif selected_stock == "VANGUARD S&P 500 ETF":
        selected_stock_ID = "VOO"
    elif selected_stock == "DOW JONES ETF":
        selected_stock_ID = "DIA"
    elif selected_stock == "RUSSELL 2000 ETF":
        selected_stock_ID = "IWM"
    else:
        selected_stock_ID = None
    return selected_stock_ID

# Get paths for model and scaler
def get_paths(stock_ID):
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
    MODELS_BASE_PATH = os.path.join(BASE_DIR, "Models/SIP")
    DATA_BASE_PATH = os.path.join(BASE_DIR, "Data/SIP/Scalers")

    model_file_extension = ".keras"
    scaler_file_extension = ".pkl"

    if stock_ID == "VOO":
        model_filename = (
            "ds=sip+s=VOO+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min+fm=vwap+sm=trade_count+tm=+r=36+sort=False+rfm=False+rsm=False+rtm=False+d=+st=none+cts=[0]+Lb=True+e=500+es=True+cb=val_accuracy+p=100+bs=128+tl=0.31953105330467224+ta=0.8718245029449463"
            + model_file_extension
        )
        model_path = os.path.join(MODELS_BASE_PATH, "NoScaler", model_filename)
        return model_path, None
    elif stock_ID == "DIA":
        model_filename = (
            "ds=sip+s=DIA+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min+fm=vwap+sm=trade_count+tm=+r=36+sort=False+rfm=False+rsm=False+rtm=False+d=+st=none+cts=[0]+Lb=True+e=500+es=True+cb=val_accuracy+p=100+bs=128+tl=0.36404281854629517+ta=0.8434399366378784"
            + model_file_extension
        )
        model_path = os.path.join(MODELS_BASE_PATH, "NoScaler", model_filename)
        return model_path, None
    elif stock_ID == "IWM":
        model_filename = (
            "ds=sip+s=IWM+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min+fm=vwap+sm=trade_count+tm=+r=36+sort=False+rfm=False+rsm=False+rtm=False+d=+st=none+cts=[0]+Lb=True+e=500+es=True+cb=val_accuracy+p=100+bs=128+tl=0.39144110679626465+ta=0.832350492477417"
            + model_file_extension
        )
        model_path = os.path.join(MODELS_BASE_PATH, "NoScaler", model_filename)
        return model_path, None
    elif stock_ID == "NVDA":
        scaler_name = "Robust"
        scaler_filename = (
            "robust_ds=sip+s=NVDA+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min"
            + scaler_file_extension
        )
        model_filename = (
            "ds=sip+s=NVDA+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min+fm=vwap+sm=trade_count+tm=+r=36+sort=False+rfm=False+rsm=False+rtm=False+d=+st=robust+cts=[0]+Lb=True+e=500+es=True+cb=val_accuracy+p=100+bs=128+tl=0.6547278761863708+ta=0.7020547986030579"
            + model_file_extension
        )
        model_path = os.path.join(MODELS_BASE_PATH, scaler_name, model_filename)
        scaler_path = os.path.join(DATA_BASE_PATH, scaler_name, scaler_filename)
        return model_path, scaler_path
    elif stock_ID == "AAPL":
        scaler_name = "MinMax"
        scaler_filename = (
            "minmax_ds=sip+s=AAPL+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min"
            + scaler_file_extension
        )
        model_filename = (
            "ds=sip+s=AAPL+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min+fm=vwap+sm=trade_count+tm=+r=36+sort=False+rfm=False+rsm=False+rtm=False+d=+st=minmax+cts=[0]+Lb=True+e=500+es=True+cb=val_accuracy+p=100+bs=128+tl=0.41606152057647705+ta=0.8365758657455444"
            + model_file_extension
        )
        model_path = os.path.join(MODELS_BASE_PATH, scaler_name, model_filename)
        scaler_path = os.path.join(DATA_BASE_PATH, scaler_name, scaler_filename)
        return model_path, scaler_path
    elif stock_ID == "MSFT":
        model_filename = (
            "ds=sip+s=MSFT+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min+fm=vwap+sm=trade_count+tm=+r=36+sort=False+rfm=False+rsm=False+rtm=False+d=+st=none+cts=[0]+Lb=True+e=500+es=True+cb=val_accuracy+p=100+bs=128+tl=0.3996354639530182+ta=0.8395842909812927"
            + model_file_extension
        )
        model_path = os.path.join(MODELS_BASE_PATH, "NoScaler", model_filename)
        return model_path, None
    elif stock_ID == "AMZN":
        scaler_name = "Robust"
        scaler_filename = (
            "robust_ds=sip+s=AMZN+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min"
            + scaler_file_extension
        )
        model_filename = (
            "ds=sip+s=AMZN+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min+fm=vwap+sm=trade_count+tm=+r=36+sort=False+rfm=False+rsm=False+rtm=False+d=+st=robust+cts=[0]+Lb=True+e=500+es=True+cb=val_accuracy+p=100+bs=128+tl=0.475951611995697+ta=0.8117924332618713"
            + model_file_extension
        )
        model_path = os.path.join(MODELS_BASE_PATH, scaler_name, model_filename)
        scaler_path = os.path.join(DATA_BASE_PATH, scaler_name, scaler_filename)
        return model_path, scaler_path
    elif stock_ID == "GOOG":
        scaler_name = "Robust"
        scaler_filename = (
            "robust_ds=sip+s=GOOG+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min"
            + scaler_file_extension
        )
        model_filename = (
            "ds=sip+s=GOOG+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min+fm=vwap+sm=trade_count+tm=+r=36+sort=False+rfm=False+rsm=False+rtm=False+d=+st=robust+cts=[0]+Lb=True+e=500+es=True+cb=val_accuracy+p=100+bs=128+tl=0.539172351360321+ta=0.813238799571991"
            + model_file_extension
        )
        model_path = os.path.join(MODELS_BASE_PATH, scaler_name, model_filename)
        scaler_path = os.path.join(DATA_BASE_PATH, scaler_name, scaler_filename)
        return model_path, scaler_path
    else:
        raise ValueError(f"Unsupported stock ID: {stock_ID}")

    return None, None


def get_data(stock_ID):
    API_KEY = os.getenv("ALPACA_API_KEY")
    SECRET_KEY = os.getenv("ALPACA_SECRET_KEY")
    BASE_URL = "https://api.alpaca.markets"

    api = tradeapi.REST(key_id=API_KEY, secret_key=SECRET_KEY, base_url=BASE_URL)

    now = datetime.now(timezone.utc)
    end_date = (now - timedelta(minutes=15)).isoformat()
    start_date = (now - timedelta(hours=3) - timedelta(minutes=15)).isoformat()

    data = api.get_bars(stock_ID, "5Min", start=start_date, end=end_date, feed="sip").df

    return data


def get_predictions(stock_ID):
    model_path, scaler_path = get_paths(stock_ID)
    scaler = None
    # Load scaler if available
    if scaler_path:
        scaler = joblib.load(scaler_path)

    data_df = get_data(stock_ID)

    X_VWAP = data_df[["vwap"]].to_numpy()
    X_Trade_Count = data_df[["trade_count"]].to_numpy()

    # Scale vwap if scaler provided, else use raw
    if scaler_path:
        X_VWAP_scaled = scaler.transform(X_VWAP)
    else:
        X_VWAP_scaled = X_VWAP

    X_combined = np.concatenate([X_VWAP_scaled, X_Trade_Count], axis=1)
    X_Tensor = np.expand_dims(X_combined, axis=0)

    model = _load_model(model_path)
    predictions = model.predict(X_Tensor)
    predictions = predictions.flatten()[0]

    decisive_sensibility = 0.5
    predicted_class = (predictions >= decisive_sensibility).astype(int)
    predicted_class = predicted_class.flatten()[0]

    return predictions, predicted_class, data_df, scaler, X_combined

@st.cache_data(show_spinner=False)
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    return {}

# Pre-load Lottie animation for bullish signal
lottie_success = load_lottie_url("https://assets9.lottiefiles.com/packages/lf20_fp7ak1to.json")

def main_predictions():
    st.header("Predictions")

    stocks = ["NVIDIA", "APPLE", "MICROSOFT", "AMAZON", "GOOGLE", "VANGUARD S&P 500 ETF", "DOW JONES ETF", "RUSSELL 2000 ETF"]
    selected_stock = st.selectbox("Select Stock/ETF:", stocks, key="predictions_stock")
    selected_stock_ID = get_stocks_ID(selected_stock)

    # Add a button to refresh predictions
    if st.button("🔄 Refresh Predictions"):
        st.rerun()

    if selected_stock_ID:
        with st.spinner(f"Generating predictions for {selected_stock_ID}..."):
            pred_pct, pred_class, df_live, scaler, X_combined = get_predictions(selected_stock_ID)
            if pred_class == 1:
                pred_pct = (pred_pct - 0.5) * 2
            else:
                pred_pct = (0.5 - pred_pct) * 2

        # Metrics
        col1, col2, col3 = st.columns([1,1,1])
        col1.metric("Next 3h Movement", "Up" if pred_class==1 else "Down", delta=f"{pred_class-1}", delta_color="normal")
        col2.metric("Certainty", f"{pred_pct:.2%}")
        col2.progress(int(pred_pct * 100))
        col3.metric("Last Updated (UTC)", pd.to_datetime(df_live.index[-1]).strftime('%Y-%m-%d %H:%M'))

        st.markdown("---")
        tabs = st.tabs(["📊 Live Chart", "🗃️ Raw Data"])

        with tabs[0]:
            features = ["Close ($)", "High ($)", "Low ($)", "Trade Count", "Open ($)", "Volume", "VWAP ($)"]
            selected_feature = st.selectbox("Select Feature:", features, key="selected_feature")
            if selected_feature == "Close":
                feature_y = "close"
            elif selected_feature == "High":
                feature_y = "high"
            elif selected_feature == "Low":
                feature_y = "low"
            elif selected_feature == "Trade Count":
                feature_y = "trade_count"
            elif selected_feature == "Open":
                feature_y = "open"
            elif selected_feature == "Volume":
                feature_y = "volume"
            else:
                feature_y = "vwap"
            fig = px.line(
                df_live, x=df_live.index, y=feature_y, title=f"{selected_stock} {selected_feature}", labels={"index":"Datetime", feature_y:selected_feature},
                template="plotly_dark", markers=True, line_shape="linear"
            )
            st.plotly_chart(fig, use_container_width=True)

        with tabs[1]:
            st.subheader("Raw Live Market Data")
            with st.expander("Show Data Table", expanded=True):
                df_live.index = pd.to_datetime(df_live.index).tz_localize(None)
                df_live.index.name = "Date & Time"
                df_live.rename(columns={
                    "close":"Close ($)","high":"High ($)","low":"Low ($)",
                    "trade_count":"Trade Count","open":"Open ($)",
                    "volume":"Volume","vwap":"VWAP ($)"
                }, inplace=True)
                st.dataframe(
                    df_live.style.format({
                        'Close':'${:,.2f}','Volume':'{:,.0f}','VWAP':'${:,.2f}'
                    })
                )

# If running this script directly (optional)
# if __name__ == '__main__':
#   main_predictions()
