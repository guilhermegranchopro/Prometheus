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
        model_path = os.path.join(MODELS_BASE_PATH, model_filename)
        return model_path, None
    elif stock_ID == "DIA":
        model_filename = (
            "ds=sip+s=DIA+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min+fm=vwap+sm=trade_count+tm=+r=36+sort=False+rfm=False+rsm=False+rtm=False+d=+st=none+cts=[0]+Lb=True+e=500+es=True+cb=val_accuracy+p=100+bs=128+tl=0.36404281854629517+ta=0.8434399366378784"
            + model_file_extension
        )
        model_path = os.path.join(MODELS_BASE_PATH, model_filename)
        return model_path, None
    elif stock_ID == "IWM":
        model_filename = (
            "ds=sip+s=IWM+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min+fm=vwap+sm=trade_count+tm=+r=36+sort=False+rfm=False+rsm=False+rtm=False+d=+st=none+cts=[0]+Lb=True+e=500+es=True+cb=val_accuracy+p=100+bs=128+tl=0.39144110679626465+ta=0.832350492477417"
            + model_file_extension
        )
        model_path = os.path.join(MODELS_BASE_PATH, model_filename)
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
        model_path = os.path.join(MODELS_BASE_PATH, model_filename)
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


def main_predictions():
    st.header("Predictions")
    stocks = ["NVDA", "AAPL", "MSFT", "AMZN", "GOOG", "VOO", "DIA", "IWM"]
    selected_stock = st.selectbox("Select Stock/ETF:", stocks, key="predictions_stock")

    if selected_stock:
        with st.spinner(
            f"Fetching data and generating prediction for {selected_stock}..."
        ):
            predictions, predicted_class, data_df, scaler, X_combined = get_predictions(
                selected_stock
            )
            predictions_str = f"{predictions:.2%}"

            # Aesthetic and comprehensive display of results
            st.subheader("Model Predictions - Next 3 Hours")
            m1, m2 = st.columns(2)
            m1.metric("Latest Prediction", f"{predicted_class}")
            m2.metric("Rate of certainty of the prediction", predictions_str)

            # Interactive Live Market Data Chart
            st.subheader("Live Market Data")
            # Expanders for raw data and features
            with st.expander("Raw Live Stock Market Data", expanded=False):
                with st.spinner("Fetching live data for..."):
                    data_df.index = pd.to_datetime(data_df.index).tz_localize(None)
                    data_df.index.name = "Date & Time"
                    data_df.rename(
                        columns={
                            "close": "Close",
                            "high": "High",
                            "low": "Low",
                            "trade_count": "Trade Count",
                            "open": "Open",
                            "volume": "Volume",
                            "vwap": "VWAP",
                        },
                        inplace=True,
                    )
                    st.dataframe(data_df)


# If running this script directly (optional)
# if __name__ == '__main__':
#   main_predictions()
