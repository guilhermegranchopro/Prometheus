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
from urllib3.exceptions import MaxRetryError
from dotenv import load_dotenv  # Import load_dotenv

# Load environment variables from .env file
load_dotenv()

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
    if selected_stock == "NVIDIA (NVDA)":
        selected_stock_ID = "NVDA"
    elif selected_stock == "APPLE (AAPL)":
        selected_stock_ID = "AAPL"
    elif selected_stock == "MICROSOFT (MSFT)":
        selected_stock_ID = "MSFT"
    elif selected_stock == "AMAZON (AMZN)":
        selected_stock_ID = "AMZN"
    elif selected_stock == "GOOGLE (GOOG)":
        selected_stock_ID = "GOOG"
    elif selected_stock == "VANGUARD S&P 500 ETF (VOO)":
        selected_stock_ID = "VOO"
    elif selected_stock == "DOW JONES ETF (DIA)":
        selected_stock_ID = "DIA"
    elif selected_stock == "RUSSELL 2000 ETF (IWM)":
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
        scaler_name = "Robust"
        scaler_filename = (
            "robust_ds=sip+s=VOO+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min"
            + scaler_file_extension
        )
        model_filename = (
            "ds=sip+s=VOO+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min+fm=vwap+sm=trade_count+tm=+r=36+sort=False+adjustment=all+rfm=False+rsm=False+rtm=False+d=+st=robust+cts=[0]+Lb=True+e=500+es=True+cb=val_accuracy+p=100+bs=128+tl=0.3559+ta=0.8741"
            + model_file_extension
        )
        scaler_path = os.path.join(DATA_BASE_PATH, scaler_name, scaler_filename)
        model_path = os.path.join(MODELS_BASE_PATH, scaler_name, model_filename)
        return model_path, scaler_path
    elif stock_ID == "DIA":
        model_filename = (
            "ds=sip+s=DIA+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min+fm=vwap+sm=trade_count+tm=+r=36+sort=False+adjustment=all+rfm=False+rsm=False+rtm=False+d=+st=none+cts=[0]+Lb=True+e=500+es=True+cb=val_accuracy+p=100+bs=128+tl=0.3716+ta=0.8385"
            + model_file_extension
        )
        model_path = os.path.join(MODELS_BASE_PATH, "NoScaler", model_filename)
        return model_path, None
    elif stock_ID == "IWM":
        model_filename = (
            "ds=sip+s=IWM+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min+fm=vwap+sm=trade_count+tm=+r=36+sort=False+adjustment=all+rfm=False+rsm=False+rtm=False+d=+st=none+cts=[0]+Lb=True+e=500+es=True+cb=val_accuracy+p=100+bs=128+tl=0.3888+ta=0.8239"
            + model_file_extension
        )
        model_path = os.path.join(MODELS_BASE_PATH, "NoScaler", model_filename)
        return model_path, None
    elif stock_ID == "NVDA":
        model_filename = (
            "ds=sip+s=NVDA+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min+fm=vwap+sm=trade_count+tm=+r=36+sort=False+adjustment=all+rfm=False+rsm=False+rtm=False+d=+st=none+cts=[0]+Lb=True+e=500+es=True+cb=val_accuracy+p=100+bs=128+tl=0.3756+ta=0.8445"
            + model_file_extension
        )
        model_path = os.path.join(MODELS_BASE_PATH, "NoScaler", model_filename)
        return model_path, None
    elif stock_ID == "AAPL":
        model_filename = (
            "ds=sip+s=AAPL+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min+fm=vwap+sm=trade_count+tm=+r=36+sort=False+adjustment=all+rfm=False+rsm=False+rtm=False+d=+st=none+cts=[0]+Lb=True+e=500+es=True+cb=val_accuracy+p=100+bs=128+tl=0.4137+ta=0.8440"
            + model_file_extension
        )
        model_path = os.path.join(MODELS_BASE_PATH, "NoScaler", model_filename)
        return model_path, None
    elif stock_ID == "MSFT":
        model_filename = (
            "ds=sip+s=MSFT+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min+fm=vwap+sm=trade_count+tm=+r=36+sort=False+adjustment=all+rfm=False+rsm=False+rtm=False+d=+st=none+cts=[0]+Lb=True+e=500+es=True+cb=val_accuracy+p=100+bs=128+tl=0.3464+ta=0.8599"
            + model_file_extension
        )
        model_path = os.path.join(MODELS_BASE_PATH, "NoScaler", model_filename)
        return model_path, None
    elif stock_ID == "AMZN":
        model_filename = (
            "ds=sip+s=AMZN+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min+fm=vwap+sm=trade_count+tm=+r=36+sort=False+adjustment=all+rfm=False+rsm=False+rtm=False+d=+st=none+cts=[0]+Lb=True+e=500+es=True+cb=val_accuracy+p=100+bs=128+tl=0.6051+ta=0.8"
            + model_file_extension
        )
        model_path = os.path.join(MODELS_BASE_PATH, "NoScaler", model_filename)
        return model_path, None
    elif stock_ID == "GOOG":
        scaler_name = "MinMax"
        scaler_filename = (
            "minmax_ds=sip+s=GOOG+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min"
            + scaler_file_extension
        )
        model_filename = (
            "ds=sip+s=GOOG+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min+fm=vwap+sm=trade_count+tm=+r=36+sort=False+adjustment=all+rfm=False+rsm=False+rtm=False+d=+st=minmax+cts=[0]+Lb=True+e=500+es=True+cb=val_accuracy+p=100+bs=128+tl=0.609+ta=0.816"
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


def get_trading_hours(POLYGON_API):
    num_of_keys = 5

    try:
        POLYGON_API += 1
        # Correct variable name construction
        env_var_name = f"POLYGON_API_KEY_{POLYGON_API}"

        API_KEY = os.getenv(env_var_name)

        # Check if the API key was loaded
        if API_KEY is None:
            # If we've tried all keys or the first key is missing, raise error
            if POLYGON_API >= num_of_keys:
                return f"Error: Polygon API Key {env_var_name} not found in environment variables or all keys failed."
            # Otherwise, try the next key
            else:
                return get_trading_hours(POLYGON_API)  # Recurse to try next key index

        client = RESTClient(API_KEY)

        status = client.get_market_status()

    except MaxRetryError as e:
        # Check if it's a rate limit error and if there are more keys to try
        if "429" in str(e) and POLYGON_API < num_of_keys:
            # Recursively call with the current index (it will be incremented at the start of the next call)
            return get_trading_hours(POLYGON_API)
        else:
            # Return error if it's not 429 or if all keys have been tried
            return None
    except (
        Exception
    ):  # Catch other potential errors during client initialization or request
        return None

    if status.market == "open":
        trading_hours_status = "The market is open regular hours."
    elif status.early_hours:
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
    raw_prediction = raw_prediction.flatten()[0]  # Keep the raw value (0.0 to 1.0)

    decisive_sensibility = 0.5
    predicted_class = (raw_prediction >= decisive_sensibility).astype(int)

    return (
        raw_prediction,
        raw_prediction,
        predicted_class,
        data_df,
        scaler,
        X_combined,
    )


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


def get_clock_emoji(dt_object):
    """Returns a clock emoji based on the hour of the datetime object."""
    hour = dt_object.hour
    # Emojis for 12, 1, 2, ..., 11 o'clock
    # 🕛 (12), 🕐 (1), 🕑 (2), 🕒 (3), 🕓 (4), 🕔 (5), 🕕 (6), 🕖 (7), 🕗 (8), 🕘 (9), 🕙 (10), 🕚 (11)
    clock_emojis = ["🕛", "🕐", "🕑", "🕒", "🕓", "🕔", "🕕", "🕖", "🕗", "🕘", "🕙", "🕚"]
    # Map 24-hour format to 12-hour emoji index
    # Hour 0 (midnight) and 12 (noon) should use 🕛 (index 0)
    # Hour 1 and 13 should use 🕐 (index 1)
    # ...
    # Hour 11 and 23 should use 🕚 (index 11)
    emoji_index = hour % 12
    return clock_emojis[emoji_index]


def main_predictions():
    st.header("📈 Stock Movement Predictions")  # Added emoji

    stocks = [
        "NVIDIA (NVDA)",
        "APPLE (AAPL)",
        "MICROSOFT (MSFT)",
        "AMAZON (AMZN)",
        "GOOGLE (GOOG)",
        "VANGUARD S&P 500 ETF (VOO)",
        "DOW JONES ETF (DIA)",
        "RUSSELL 2000 ETF (IWM)",
    ]
    selected_stock = st.selectbox("Select Stock/ETF:", stocks, key="predictions_stock")
    selected_stock_ID = get_stocks_ID(selected_stock)

    # Initialize session state for help message visibility
    if "show_help_message" not in st.session_state:
        st.session_state.show_help_message = False

    # Add a button to refresh predictions
    if st.button("🔄 Refresh Predictions"):
        # Reset help message visibility on refresh
        st.session_state.show_help_message = False
        st.rerun()

    if selected_stock_ID:
        # Fetch market status first and handle potential errors
        # Start with index 0, the function will increment it to 1 for the first key
        market_status = get_trading_hours(0)

        # Display market status or error message
        current_utc_time = datetime.now(timezone.utc)
        clock_emoji = get_clock_emoji(current_utc_time)
        st.subheader(
            f"{clock_emoji} Last Updated: {pd.to_datetime(current_utc_time).strftime('%Y-%m-%d %H:%M')} (UTC)"
        )

        if market_status is None:
            pass
        elif "open regular hours" in market_status:
            st.success(f"📊 Market Status: {market_status}")
        elif "pre hours" in market_status:
            st.info("⏳ Market Status: The market is open for pre-market trading.")
        elif "after hours" in market_status:
            st.warning("⏳ Market Status: The market is open for after-hours trading.")
        else:
            st.error(f"⛔ Market Status: The market is {market_status}")

        # Only proceed with predictions if market status was fetched successfully
        if not market_status.startswith("Error:"):
            with st.spinner(
                f"🧠 Generating predictions for {selected_stock_ID}..."
            ):  # Added emoji
                # Get raw prediction, certainty percentage, and class
                raw_pred, pred_certainty, pred_class, df_live, scaler, X_combined = (
                    get_predictions(selected_stock_ID)
                )

            # Add vertical space using HTML line breaks instead of horizontal rules
            st.markdown("<br>" * 1, unsafe_allow_html=True)

            col1, col2, col3 = st.columns([0.5, 3, 0.5])  # Adjusted column ratios

            with col3:
                if st.button("Help", help="Click to toggle help.", use_container_width=False):
                    st.session_state.show_help_message = not st.session_state.show_help_message
            
            # Display help message below columns if toggled
            if st.session_state.show_help_message:
                # Add vertical space using HTML line breaks instead of horizontal rules
                st.markdown("<br>" * 3, unsafe_allow_html=True)
                st.info(
                    """
                    **Understanding the Prediction Bar:**

                    - **Next 3h Prediction:** Indicates the anticipated price movement (Up ⬆️ or Down ⬇️) for the selected stock/ETF over the next approximately 3 hours.
                    - **Certainty:** The model's confidence in this prediction, shown as a percentage. A higher percentage means greater confidence.
                    - **Marker Position:** The white marker on the gradient bar visually represents this certainty. It moves from left (Down) to right (Up).
                    - **Gradient Bar:** Ranges from red (strong Down prediction) to green (strong Up prediction).
                    - **Raw Value:** The direct output from the prediction model (a value between 0.0 and 1.0). Values closer to 1.0 suggest an 'Up' movement, while values closer to 0.0 suggest a 'Down' movement. 0.5 is the neutral point.
                    - **Help Button:** Click the Help button to toggle this message on or off.

                    """
                )

            with col2:
                # --- Reverted marker position calculation ---
                # Calculate marker position based on certainty and class
                if pred_class == 1:  # Up
                    tooltip_text = f"Predicted UP with {pred_certainty:.1%} certainty (Raw: {raw_pred:.3f})"
                else:  # Down
                    tooltip_text = f"Predicted DOWN with {pred_certainty:.1%} certainty (Raw: {raw_pred:.3f})"

                # Format the certainty percentage for display
                marker_position_pct = pred_certainty * 100
                certainty_display = f"{pred_certainty:.1%}"

                # Ensure position is within bounds (0-100)
                marker_position_pct = max(0, min(100, marker_position_pct))

                # Custom HTML/CSS for the prediction bar
                bar_html = f"""
                <div style="font-family: sans-serif; margin-top: 10px; margin-bottom: 50px; text-align: center; font-weight: bold; font-size: 1.3em;">
                    Next 3h {selected_stock_ID} Price Movement Prediction<br>{pd.to_datetime(current_utc_time - timedelta(minutes=15)).strftime('%H:%M')} - {pd.to_datetime(current_utc_time + timedelta(hours=2) + timedelta(minutes=45)).strftime('%H:%M')} (UTC)
                </div>
                <div style="display: flex; align-items: center; justify-content: space-between; width: 100%; margin-bottom: 5px;">
                    <span style="color: white; font-weight: bold; font-size: 1.1em; margin-right: 5px;">⬇️ Down</span>
                    <div style="position: relative; height: 45px; flex-grow: 1; border-radius: 5px; background: linear-gradient(to right, #b71c1c, #1b5e20); box-sizing: border-box;">
                        <div title="{tooltip_text}" style="position: absolute; left: {marker_position_pct}%; top: -25px; transform: translateX(-50%); background-color: #444; color: white; padding: 3px 8px; border-radius: 4px; font-size: 0.9em; white-space: nowrap;">
                            {certainty_display} Certainty
                        </div>
                        <div title="{tooltip_text}" style="position: absolute; left: {marker_position_pct}%; top: 50%; transform: translate(-50%, -50%); width: 4px; height: 30px; background-color: white; border-radius: 2px; box-shadow: 0 0 5px rgba(0,0,0,0.5);"></div>
                        <div title="{tooltip_text}" style="position: absolute; left: {marker_position_pct}%; bottom: -25px; transform: translateX(-50%); font-size: 1.5em;">
                            {"⬆️" if pred_class == 1 else "⬇️"}
                        </div>
                    </div>
                    <span style="color: white; font-weight: bold; font-size: 1.1em; margin-left: 5px;">Up ⬆️</span>
                </div>
                """
                st.markdown(bar_html, unsafe_allow_html=True)

            # Add vertical space using HTML line breaks instead of horizontal rules
            st.markdown("<br>" * 3, unsafe_allow_html=True)

            tabs = st.tabs(["📊 Live Chart", "🗃️ Raw Data"])

            with tabs[0]:
                st.subheader("📊 Live Market Chart")  # Added emoji
                features = [
                    "VWAP (USD)",
                    "Close (USD)",
                    "High (USD)",
                    "Low (USD)",
                    "Trade Count",
                    "Open (USD)",
                    "Volume",
                ]
                selected_feature = st.selectbox(
                    "Select Feature:", features, key="selected_feature"
                )
                if selected_feature == "Close (USD)":
                    feature_y = "close"
                elif selected_feature == "High (USD)":
                    feature_y = "high"
                elif selected_feature == "Low (USD)":
                    feature_y = "low"
                elif selected_feature == "Trade Count":
                    feature_y = "trade_count"
                elif selected_feature == "Open (USD)":
                    feature_y = "open"
                elif selected_feature == "Volume":
                    feature_y = "volume"
                else:
                    feature_y = "vwap"

                fig = px.line(
                    df_live,
                    x=df_live.index,
                    y=feature_y,
                    title=f"{selected_stock} - {selected_feature}",
                    labels={"index": "Datetime (UTC)", feature_y: selected_feature},
                    template="plotly_dark",
                    markers=True,
                    line_shape="spline",
                )
                fig.update_layout(
                    title_x=0.5,
                    xaxis_title="Datetime (UTC)",
                    yaxis_title=selected_feature,
                )
                st.plotly_chart(fig, use_container_width=True)

            with tabs[1]:
                st.subheader("🗃️ Raw Live Market Data")  # Added emoji
                with st.expander("Show Data Table", expanded=True):
                    df_display = df_live.copy()
                    df_display.index = pd.to_datetime(df_display.index).tz_localize(
                        None
                    )
                    df_display.index.name = "Date & Time"
                    df_display.rename(
                        columns={
                            "close": "Close (USD)",
                            "high": "High (USD)",
                            "low": "Low (USD)",
                            "trade_count": "Trade Count",
                            "open": "Open (USD)",
                            "volume": "Volume",
                            "vwap": "VWAP (USD)",
                        },
                        inplace=True,
                    )
                    df_display = df_display[
                        [
                            "Open (USD)",
                            "High (USD)",
                            "Low (USD)",
                            "Close (USD)",
                            "Volume",
                            "Trade Count",
                            "VWAP (USD)",
                        ]
                    ]
                    st.dataframe(
                        df_display.style.format(
                            {
                                "Open (USD)": "${:,.2f}",
                                "High (USD)": "${:,.2f}",
                                "Low (USD)": "${:,.2f}",
                                "Close (USD)": "${:,.2f}",
                                "Volume": "{:,.0f}",
                                "VWAP (USD)": "${:,.2f}",
                            }
                        ),
                        use_container_width=True,
                    )
