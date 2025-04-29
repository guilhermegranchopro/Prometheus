import os
import sys
import importlib
import streamlit as st
import contextlib
import numpy as np
import joblib
import alpaca_trade_api as tradeapi
from polygon import RESTClient
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

    delay_safe_df = 5
    df_size = 36

    api = tradeapi.REST(key_id=API_KEY, secret_key=SECRET_KEY, base_url=BASE_URL)

    now = datetime.now(timezone.utc)
    start_date = (now - timedelta(days=delay_safe_df)).isoformat()

    data = api.get_bars(stock_ID, "5Min", start=start_date, feed="sip").df.tail(df_size)

    return data

def get_trading_hours():
    API_KEY = os.getenv("POLYGON_API_KEY")

    client = RESTClient(API_KEY)

    status = client.get_market_status()

    if status.market == "open":
        trading_hours_status = "The market is open regular hours."
    elif status.pearly_hours:
        trading_hours_status = "The market is open pre hours."
    elif status.after_hours:
        trading_hours_status = "The market is open after hours."
    else:
        trading_hours_status = "The market is closed."

    return trading_hours_status


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
    raw_prediction = model.predict(X_Tensor)
    raw_prediction = raw_prediction.flatten()[0] # Keep the raw value (0.0 to 1.0)

    decisive_sensibility = 0.5
    predicted_class = (raw_prediction >= decisive_sensibility).astype(int)
    # predicted_class = predicted_class.flatten()[0] # Already flattened

    return raw_prediction, raw_prediction, predicted_class, data_df, scaler, X_combined # Return raw_prediction and certainty_pct


@st.cache_data(show_spinner=False)
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    return {}


# Pre-load Lottie animation for bullish signal
lottie_success = load_lottie_url(
    "https://assets9.lottiefiles.com/packages/lf20_fp7ak1to.json"
)


def main_predictions():
    st.header("📈 Stock Movement Predictions")  # Added emoji

    # Get and display market status
    market_status = get_trading_hours()
    if "open regular hours" in market_status:
        st.success(f"📊 Market Status: {market_status}")
    elif "pre hours" in market_status or "after hours" in market_status:
        st.warning(f"⏳ Market Status: {market_status}")
    else:
        st.error(f"⛔ Market Status: {market_status}")

    stocks = [
        "NVIDIA",
        "APPLE",
        "MICROSOFT",
        "AMAZON",
        "GOOGLE",
        "VANGUARD S&P 500 ETF",
        "DOW JONES ETF",
        "RUSSELL 2000 ETF",
    ]
    selected_stock = st.selectbox("Select Stock/ETF:", stocks, key="predictions_stock")
    selected_stock_ID = get_stocks_ID(selected_stock)

    # Add a button to refresh predictions
    if st.button("🔄 Refresh Predictions"):
        st.rerun()

    if selected_stock_ID:
        with st.spinner(
            f"🧠 Generating predictions for {selected_stock_ID}..."
        ):  # Added emoji
            # Get raw prediction, certainty percentage, and class
            raw_pred, pred_certainty, pred_class, df_live, scaler, X_combined = get_predictions(
                selected_stock_ID)

        # Metrics and Lottie Animation
        st.subheader(
            f"Last Updated: {pd.to_datetime(datetime.now(timezone.utc)).strftime('%Y-%m-%d %H:%M')} (UTC)"
        )

        # Add vertical space using HTML line breaks instead of horizontal rules
        st.markdown("<br>" * 1, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 3, 1])  # Adjusted column ratios

        with col2:
            # --- Reverted marker position calculation ---
            # Calculate marker position based on certainty and class
            if pred_class == 1: # Up
                tooltip_text = f"Predicted UP with {pred_certainty:.1%} certainty (Raw: {raw_pred:.3f})"
            else: # Down
                tooltip_text = f"Predicted DOWN with {pred_certainty:.1%} certainty (Raw: {raw_pred:.3f})"

            # Format the certainty percentage for display
            marker_position_pct = pred_certainty*100
            certainty_display = f"{pred_certainty:.1%}"

            # Ensure position is within bounds (0-100)
            marker_position_pct = max(0, min(100, marker_position_pct))

            # Custom HTML/CSS for the prediction bar
            bar_html = f"""
            <div style="font-family: sans-serif; margin-top: 10px; margin-bottom: 50px; text-align: center; font-weight: bold; font-size: 1.3em;">
                Next 3h Movement Prediction
            </div>
            <div style="display: flex; align-items: center; justify-content: space-between; width: 100%; margin-bottom: 5px;">
                <span style="color: white; font-weight: bold; font-size: 1.1em; margin-right: 5px;">⬇️ Down</span>
                <div style="position: relative; height: 45px; flex-grow: 1; border-radius: 5px; background: linear-gradient(to right, #b71c1c, #1b5e20); box-sizing: border-box;">
                    <div title="{tooltip_text}" style="position: absolute; left: {marker_position_pct}%; top: -25px; transform: translateX(-50%); background-color: #444; color: white; padding: 3px 8px; border-radius: 4px; font-size: 0.9em; white-space: nowrap;">
                        {certainty_display} Certainty
                    </div>
                    <div title="{tooltip_text}" style="position: absolute; left: {marker_position_pct}%; top: 50%; transform: translate(-50%, -50%); width: 4px; height: 30px; background-color: white; border-radius: 2px; box-shadow: 0 0 5px rgba(0,0,0,0.5);"></div>
                    <div title="{tooltip_text}" style="position: absolute; left: {marker_position_pct}%; bottom: -25px; transform: translateX(-50%); font-size: 1.5em;">
                        {'⬆️' if pred_class == 1 else '⬇️'}
                    </div>
                </div>
                <span style="color: white; font-weight: bold; font-size: 1.1em; margin-left: 5px;">Up ⬆️</span>
            </div>
            """
            st.markdown(bar_html, unsafe_allow_html=True)
            # Removed st.progress bar as certainty is now on the custom bar

        # Add vertical space using HTML line breaks instead of horizontal rules
        st.markdown("<br>" * 3, unsafe_allow_html=True) 
        
        tabs = st.tabs(["📊 Live Chart", "🗃️ Raw Data"])

        with tabs[0]:
            st.subheader("📊 Live Market Chart")  # Added emoji
            features = [
                "VWAP ($)",
                "Close ($)",
                "High ($)",
                "Low ($)",
                "Trade Count",
                "Open ($)",
                "Volume",
            ]  # Changed default
            selected_feature = st.selectbox(
                "Select Feature:", features, key="selected_feature"
            )
            # ... existing feature mapping logic ...
            if selected_feature == "Close ($)":
                feature_y = "close"
            elif selected_feature == "High ($)":
                feature_y = "high"
            elif selected_feature == "Low ($)":
                feature_y = "low"
            elif selected_feature == "Trade Count":
                feature_y = "trade_count"
            elif selected_feature == "Open ($)":
                feature_y = "open"
            elif selected_feature == "Volume":
                feature_y = "volume"
            else:  # Default to VWAP
                feature_y = "vwap"

            fig = px.line(
                df_live,
                x=df_live.index,
                y=feature_y,
                title=f"{selected_stock} - {selected_feature}",
                labels={"index": "Datetime (UTC)", feature_y: selected_feature},
                template="plotly_dark",
                markers=True,
                line_shape="spline",  # Changed line_shape to spline
            )
            fig.update_layout(title_x=0.5)  # Center title
            st.plotly_chart(fig, use_container_width=True)

        with tabs[1]:
            st.subheader("🗃️ Raw Live Market Data")  # Added emoji
            with st.expander(
                "Show Data Table", expanded=False
            ):  # Set expanded to False initially
                df_display = df_live.copy()  # Work on a copy
                df_display.index = pd.to_datetime(df_display.index).tz_localize(
                    None
                )  # Remove timezone for display
                df_display.index.name = "Date & Time"
                df_display.rename(
                    columns={
                        "close": "Close ($)",
                        "high": "High ($)",
                        "low": "Low ($)",
                        "trade_count": "Trade Count",
                        "open": "Open ($)",
                        "volume": "Volume",
                        "vwap": "VWAP ($)",
                    },
                    inplace=True,
                )
                # Reorder columns for better readability
                df_display = df_display[
                    [
                        "Open ($)",
                        "High ($)",
                        "Low ($)",
                        "Close ($)",
                        "Volume",
                        "Trade Count",
                        "VWAP ($)",
                    ]
                ]
                st.dataframe(
                    df_display.style.format(
                        {
                            "Open ($)": "${:,.2f}",
                            "High ($)": "${:,.2f}",
                            "Low ($)": "${:,.2f}",
                            "Close ($)": "${:,.2f}",
                            "Volume": "{:,.0f}",
                            "VWAP ($)": "${:,.2f}",
                        }
                    ),
                    use_container_width=True,  # Make dataframe use full width
                )
