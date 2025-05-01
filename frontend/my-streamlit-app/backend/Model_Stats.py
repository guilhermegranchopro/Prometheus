import streamlit as st
import os
from backend.Predictions import get_stocks_ID


def get_paths(stock_ID):
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
    IMAGES_BASE_PATH = os.path.join(BASE_DIR, "Simons/Images/SIP")

    images_file_extension = ".png"

    if stock_ID == "VOO":
        accuracy_curve_filename = (
            "a_ds=sip+s=VOO+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min+fm=vwap+sm=trade_count+tm=+r=36+sort=False+adjustment=all+rfm=False+rsm=False+rtm=False+d=+st=robust+cts=[0]+Lb=True+e=500+es=True+cb=val_accuracy+p=100+bs=128+tl=0.3559+ta=0.8741"
            + images_file_extension
        )
        loss_curve_filename = (
            "l_ds=sip+s=VOO+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min+fm=vwap+sm=trade_count+tm=+r=36+sort=False+adjustment=all+rfm=False+rsm=False+rtm=False+d=+st=robust+cts=[0]+Lb=True+e=500+es=True+cb=val_accuracy+p=100+bs=128+tl=0.3559+ta=0.8741"
            + images_file_extension
        )
        confusion_matrix_filename = (
            "cm_ds=sip+s=VOO+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min+fm=vwap+sm=trade_count+tm=+r=36+sort=False+adjustment=all+rfm=False+rsm=False+rtm=False+d=+st=robust+cts=[0]+Lb=True+e=500+es=True+cb=val_accuracy+p=100+bs=128+tl=0.3559+ta=0.8741"
            + images_file_extension
        )
        accuracy_curve_path = os.path.join(
            IMAGES_BASE_PATH, "Robust", accuracy_curve_filename
        )
        loss_curve_path = os.path.join(IMAGES_BASE_PATH, "Robust", loss_curve_filename)
        confusion_matrix_path = os.path.join(
            IMAGES_BASE_PATH, "Robust", confusion_matrix_filename
        )
        test_accuracy = 0.8741
        test_loss = 0.3559
        return (
            accuracy_curve_path,
            loss_curve_path,
            confusion_matrix_path,
            test_accuracy,
            test_loss,
        )
    elif stock_ID == "DIA":
        accuracy_curve_filename = (
            "a_ds=sip+s=DIA+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min+fm=vwap+sm=trade_count+tm=+r=36+sort=False+adjustment=all+rfm=False+rsm=False+rtm=False+d=+st=none+cts=[0]+Lb=True+e=500+es=True+cb=val_accuracy+p=100+bs=128+tl=0.3716+ta=0.8385"
            + images_file_extension
        )
        loss_curve_filename = (
            "l_ds=sip+s=DIA+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min+fm=vwap+sm=trade_count+tm=+r=36+sort=False+adjustment=all+rfm=False+rsm=False+rtm=False+d=+st=none+cts=[0]+Lb=True+e=500+es=True+cb=val_accuracy+p=100+bs=128+tl=0.3716+ta=0.8385"
            + images_file_extension
        )
        confusion_matrix_filename = (
            "cm_ds=sip+s=DIA+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min+fm=vwap+sm=trade_count+tm=+r=36+sort=False+adjustment=all+rfm=False+rsm=False+rtm=False+d=+st=none+cts=[0]+Lb=True+e=500+es=True+cb=val_accuracy+p=100+bs=128+tl=0.3716+ta=0.8385"
            + images_file_extension
        )
        accuracy_curve_path = os.path.join(
            IMAGES_BASE_PATH, "NoScaler", accuracy_curve_filename
        )
        loss_curve_path = os.path.join(
            IMAGES_BASE_PATH, "NoScaler", loss_curve_filename
        )
        confusion_matrix_path = os.path.join(
            IMAGES_BASE_PATH, "NoScaler", confusion_matrix_filename
        )
        test_accuracy = 0.8390
        test_loss = 0.3716
        return (
            accuracy_curve_path,
            loss_curve_path,
            confusion_matrix_path,
            test_accuracy,
            test_loss,
        )
    elif stock_ID == "IWM":
        accuracy_curve_filename = (
            "a_ds=sip+s=IWM+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min+fm=vwap+sm=trade_count+tm=+r=36+sort=False+adjustment=all+rfm=False+rsm=False+rtm=False+d=+st=none+cts=[0]+Lb=True+e=500+es=True+cb=val_accuracy+p=100+bs=128+tl=0.3888+ta=0.8239"
            + images_file_extension
        )
        loss_curve_filename = (
            "l_ds=sip+s=IWM+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min+fm=vwap+sm=trade_count+tm=+r=36+sort=False+adjustment=all+rfm=False+rsm=False+rtm=False+d=+st=none+cts=[0]+Lb=True+e=500+es=True+cb=val_accuracy+p=100+bs=128+tl=0.3888+ta=0.8239"
            + images_file_extension
        )
        confusion_matrix_filename = (
            "cm_ds=sip+s=IWM+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min+fm=vwap+sm=trade_count+tm=+r=36+sort=False+adjustment=all+rfm=False+rsm=False+rtm=False+d=+st=none+cts=[0]+Lb=True+e=500+es=True+cb=val_accuracy+p=100+bs=128+tl=0.3888+ta=0.8239"
            + images_file_extension
        )
        accuracy_curve_path = os.path.join(
            IMAGES_BASE_PATH, "NoScaler", accuracy_curve_filename
        )
        loss_curve_path = os.path.join(
            IMAGES_BASE_PATH, "NoScaler", loss_curve_filename
        )
        confusion_matrix_path = os.path.join(
            IMAGES_BASE_PATH, "NoScaler", confusion_matrix_filename
        )
        test_accuracy = 0.8239
        test_loss = 0.3888
        return (
            accuracy_curve_path,
            loss_curve_path,
            confusion_matrix_path,
            test_accuracy,
            test_loss,
        )
    elif stock_ID == "NVDA":
        accuracy_curve_filename = (
            "a_ds=sip+s=NVDA+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min+fm=vwap+sm=trade_count+tm=+r=36+sort=False+adjustment=all+rfm=False+rsm=False+rtm=False+d=+st=none+cts=[0]+Lb=True+e=500+es=True+cb=val_accuracy+p=100+bs=128+tl=0.3756+ta=0.8445"
            + images_file_extension
        )
        loss_curve_filename = (
            "l_ds=sip+s=NVDA+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min+fm=vwap+sm=trade_count+tm=+r=36+sort=False+adjustment=all+rfm=False+rsm=False+rtm=False+d=+st=none+cts=[0]+Lb=True+e=500+es=True+cb=val_accuracy+p=100+bs=128+tl=0.3756+ta=0.8445"
            + images_file_extension
        )
        confusion_matrix_filename = (
            "cm_ds=sip+s=NVDA+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min+fm=vwap+sm=trade_count+tm=+r=36+sort=False+adjustment=all+rfm=False+rsm=False+rtm=False+d=+st=none+cts=[0]+Lb=True+e=500+es=True+cb=val_accuracy+p=100+bs=128+tl=0.3756+ta=0.8445"
            + images_file_extension
        )
        accuracy_curve_path = os.path.join(
            IMAGES_BASE_PATH, "NoScaler", accuracy_curve_filename
        )
        loss_curve_path = os.path.join(
            IMAGES_BASE_PATH, "NoScaler", loss_curve_filename
        )
        confusion_matrix_path = os.path.join(
            IMAGES_BASE_PATH, "NoScaler", confusion_matrix_filename
        )
        test_accuracy = 0.8445
        test_loss = 0.3756
        return (
            accuracy_curve_path,
            loss_curve_path,
            confusion_matrix_path,
            test_accuracy,
            test_loss,
        )
    elif stock_ID == "AAPL":
        accuracy_curve_filename = (
            "a_ds=sip+s=AAPL+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min+fm=vwap+sm=trade_count+tm=+r=36+sort=False+adjustment=all+rfm=False+rsm=False+rtm=False+d=+st=none+cts=[0]+Lb=True+e=500+es=True+cb=val_accuracy+p=100+bs=128+tl=0.4137+ta=0.844"
            + images_file_extension
        )
        loss_curve_filename = (
            "l_ds=sip+s=AAPL+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min+fm=vwap+sm=trade_count+tm=+r=36+sort=False+adjustment=all+rfm=False+rsm=False+rtm=False+d=+st=none+cts=[0]+Lb=True+e=500+es=True+cb=val_accuracy+p=100+bs=128+tl=0.4137+ta=0.844"
            + images_file_extension
        )
        confusion_matrix_filename = (
            "cm_ds=sip+s=AAPL+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min+fm=vwap+sm=trade_count+tm=+r=36+sort=False+adjustment=all+rfm=False+rsm=False+rtm=False+d=+st=none+cts=[0]+Lb=True+e=500+es=True+cb=val_accuracy+p=100+bs=128+tl=0.4137+ta=0.844"
            + images_file_extension
        )
        accuracy_curve_path = os.path.join(
            IMAGES_BASE_PATH, "NoScaler", accuracy_curve_filename
        )
        loss_curve_path = os.path.join(
            IMAGES_BASE_PATH, "NoScaler", loss_curve_filename
        )
        confusion_matrix_path = os.path.join(
            IMAGES_BASE_PATH, "NoScaler", confusion_matrix_filename
        )
        test_accuracy = 0.8440
        test_loss = 0.4137
        return (
            accuracy_curve_path,
            loss_curve_path,
            confusion_matrix_path,
            test_accuracy,
            test_loss,
        )
    elif stock_ID == "MSFT":
        accuracy_curve_filename = (
            "a_ds=sip+s=MSFT+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min+fm=vwap+sm=trade_count+tm=+r=36+sort=False+adjustment=all+rfm=False+rsm=False+rtm=False+d=+st=none+cts=[0]+Lb=True+e=500+es=True+cb=val_accuracy+p=100+bs=128+tl=0.3464+ta=0.8599"
            + images_file_extension
        )
        loss_curve_filename = (
            "l_ds=sip+s=MSFT+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min+fm=vwap+sm=trade_count+tm=+r=36+sort=False+adjustment=all+rfm=False+rsm=False+rtm=False+d=+st=none+cts=[0]+Lb=True+e=500+es=True+cb=val_accuracy+p=100+bs=128+tl=0.3464+ta=0.8599"
            + images_file_extension
        )
        confusion_matrix_filename = (
            "cm_ds=sip+s=MSFT+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min+fm=vwap+sm=trade_count+tm=+r=36+sort=False+adjustment=all+rfm=False+rsm=False+rtm=False+d=+st=none+cts=[0]+Lb=True+e=500+es=True+cb=val_accuracy+p=100+bs=128+tl=0.3464+ta=0.8599"
            + images_file_extension
        )
        accuracy_curve_path = os.path.join(
            IMAGES_BASE_PATH, "NoScaler", accuracy_curve_filename
        )
        loss_curve_path = os.path.join(
            IMAGES_BASE_PATH, "NoScaler", loss_curve_filename
        )
        confusion_matrix_path = os.path.join(
            IMAGES_BASE_PATH, "NoScaler", confusion_matrix_filename
        )
        test_accuracy = 0.8599
        test_loss = 0.3464
        return (
            accuracy_curve_path,
            loss_curve_path,
            confusion_matrix_path,
            test_accuracy,
            test_loss,
        )
    elif stock_ID == "AMZN":
        accuracy_curve_filename = (
            "a_ds=sip+s=AMZN+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min+fm=vwap+sm=trade_count+tm=+r=36+sort=False+adjustment=all+rfm=False+rsm=False+rtm=False+d=+st=none+cts=[0]+Lb=True+e=500+es=True+cb=val_accuracy+p=100+bs=128+tl=0.6051+ta=0.8"
            + images_file_extension
        )
        loss_curve_filename = (
            "l_ds=sip+s=AMZN+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min+fm=vwap+sm=trade_count+tm=+r=36+sort=False+adjustment=all+rfm=False+rsm=False+rtm=False+d=+st=none+cts=[0]+Lb=True+e=500+es=True+cb=val_accuracy+p=100+bs=128+tl=0.6051+ta=0.8"
            + images_file_extension
        )
        confusion_matrix_filename = (
            "cm_ds=sip+s=AMZN+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min+fm=vwap+sm=trade_count+tm=+r=36+sort=False+adjustment=all+rfm=False+rsm=False+rtm=False+d=+st=none+cts=[0]+Lb=True+e=500+es=True+cb=val_accuracy+p=100+bs=128+tl=0.6051+ta=0.8"
            + images_file_extension
        )
        accuracy_curve_path = os.path.join(
            IMAGES_BASE_PATH, "NoScaler", accuracy_curve_filename
        )
        loss_curve_path = os.path.join(
            IMAGES_BASE_PATH, "NoScaler", loss_curve_filename
        )
        confusion_matrix_path = os.path.join(
            IMAGES_BASE_PATH, "NoScaler", confusion_matrix_filename
        )
        test_accuracy = 0.8000
        test_loss = 0.6051
        return (
            accuracy_curve_path,
            loss_curve_path,
            confusion_matrix_path,
            test_accuracy,
            test_loss,
        )
    elif stock_ID == "GOOG":
        accuracy_curve_filename = (
            "a_ds=sip+s=GOOG+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min+fm=vwap+sm=trade_count+tm=+r=36+sort=False+adjustment=all+rfm=False+rsm=False+rtm=False+d=+st=minmax+cts=[0]+Lb=True+e=500+es=True+cb=val_accuracy+p=100+bs=128+tl=0.609+ta=0.816"
            + images_file_extension
        )
        loss_curve_filename = (
            "l_ds=sip+s=GOOG+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min+fm=vwap+sm=trade_count+tm=+r=36+sort=False+adjustment=all+rfm=False+rsm=False+rtm=False+d=+st=minmax+cts=[0]+Lb=True+e=500+es=True+cb=val_accuracy+p=100+bs=128+tl=0.609+ta=0.816"
            + images_file_extension
        )
        confusion_matrix_filename = (
            "cm_ds=sip+s=GOOG+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min+fm=vwap+sm=trade_count+tm=+r=36+sort=False+adjustment=all+rfm=False+rsm=False+rtm=False+d=+st=minmax+cts=[0]+Lb=True+e=500+es=True+cb=val_accuracy+p=100+bs=128+tl=0.609+ta=0.816"
            + images_file_extension
        )
        accuracy_curve_path = os.path.join(
            IMAGES_BASE_PATH, "MinMax", accuracy_curve_filename
        )
        loss_curve_path = os.path.join(IMAGES_BASE_PATH, "MinMax", loss_curve_filename)
        confusion_matrix_path = os.path.join(
            IMAGES_BASE_PATH, "MinMax", confusion_matrix_filename
        )
        test_accuracy = 0.8160
        test_loss = 0.6090
        return (
            accuracy_curve_path,
            loss_curve_path,
            confusion_matrix_path,
            test_accuracy,
            test_loss,
        )
    else:
        raise ValueError(f"Unsupported stock ID: {stock_ID}")

    return None, None, None, None, None


# Streamlit app for displaying model statistics
def main_model_stats():
    # Main header
    st.markdown("## 📊 Model Statistics Dashboard", unsafe_allow_html=True)

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
    selected_stock = st.selectbox("Select Stock/ETF:", stocks, key="model_stats_stock")
    selected_stock_ID = get_stocks_ID(selected_stock)

    if selected_stock_ID:
        st.subheader(f"✨ Performance Metrics for **{selected_stock}**")

        # Loading spinner
        with st.spinner(f"Loading data for {selected_stock}..."):
            (
                accuracy_curve_path,
                loss_curve_path,
                confusion_matrix_path,
                test_accuracy,
                test_loss,
            ) = get_paths(selected_stock_ID)

        # Display metrics with styled cards and progress
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.metric(label="Test Accuracy", value=f"{test_accuracy*100:.2f}%")
            st.progress(int(test_accuracy * 100))
            st.markdown("</div>", unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.metric(label="Test Loss", value=f"{test_loss:.4f}")
            st.markdown("</div>", unsafe_allow_html=True)

        st.divider()

        # Model Training History & Evaluation with tabs
        tabs = st.tabs(["🎨 Curves", "🧮 Confusion Matrix"])
        with tabs[0]:
            st.subheader("Accuracy & Loss Curves 📈")
            cols = st.columns(2)
            with cols[0]:
                st.image(
                    accuracy_curve_path,
                    caption=f"{selected_stock} Accuracy Curve",
                    use_container_width=True,
                )
            with cols[1]:
                st.image(
                    loss_curve_path,
                    caption=f"{selected_stock} Loss Curve",
                    use_container_width=True,
                )
        with tabs[1]:
            st.subheader("Confusion Matrix 🧩")
            col1_cm, col2_cm, col3_cm = st.columns(
                [1, 2, 1]
            )  # Adjust columns to center the confusion matrix
            with col2_cm:
                st.image(
                    confusion_matrix_path,
                    caption=f"{selected_stock} Confusion Matrix",
                    use_container_width=True,
                )


# If running this script directly (optional)
# if __name__ == "__main__":
#     main_model_stats()
