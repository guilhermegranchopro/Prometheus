import streamlit as st
import os

def get_paths(stock_ID):
    BASE_DIR_MD = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    MODELS_BASE_PATH = os.path.join(BASE_DIR_MD, "Models/SIP")
    DATA_BASE_PATH = os.path.join(BASE_DIR_MD, "Data/SIP/Scalers")

    model_file_extension = ".keras"
    scaler_file_extension = ".pkl"

    if stock_ID == "VOO":
        model_filename = "ds=sip+s=VOO+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min+fm=vwap+sm=trade_count+tm=+r=36+sort=False+rfm=False+rsm=False+rtm=False+d=+st=none+cts=[0]+Lb=True+e=500+es=True+cb=val_accuracy+p=100+bs=128+tl=0.31953105330467224+ta=0.8718245029449463" + model_file_extension
        model_path = os.path.join(MODELS_BASE_PATH, model_filename)
        return model_path, None
    elif stock_ID == "DIA":
        model_filename = "ds=sip+s=DIA+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min+fm=vwap+sm=trade_count+tm=+r=36+sort=False+rfm=False+rsm=False+rtm=False+d=+st=none+cts=[0]+Lb=True+e=500+es=True+cb=val_accuracy+p=100+bs=128+tl=0.36404281854629517+ta=0.8434399366378784" + model_file_extension
        model_path = os.path.join(MODELS_BASE_PATH, model_filename)
        return model_path, None
    elif stock_ID == "IWM":
        model_filename = "ds=sip+s=IWM+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min+fm=vwap+sm=trade_count+tm=+r=36+sort=False+rfm=False+rsm=False+rtm=False+d=+st=none+cts=[0]+Lb=True+e=500+es=True+cb=val_accuracy+p=100+bs=128+tl=0.39144110679626465+ta=0.832350492477417" + model_file_extension
        model_path = os.path.join(MODELS_BASE_PATH, model_filename)
        return model_path, None
    elif stock_ID == "NVDA":
        scaler_name = "Robust"
        scaler_filename = "robust_ds=sip+s=NVDA+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min" + scaler_file_extension
        model_filename = "ds=sip+s=NVDA+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min+fm=vwap+sm=trade_count+tm=+r=36+sort=False+rfm=False+rsm=False+rtm=False+d=+st=robust+cts=[0]+Lb=True+e=500+es=True+cb=val_accuracy+p=100+bs=128+tl=0.6547278761863708+ta=0.7020547986030579" + model_file_extension
        model_path = os.path.join(MODELS_BASE_PATH, scaler_name, model_filename)
        scaler_path = os.path.join(DATA_BASE_PATH, scaler_name, scaler_filename)
        return model_path, scaler_path
    elif stock_ID == "AAPL":
        scaler_name = "MinMax"
        scaler_filename = "minmax_ds=sip+s=AAPL+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min" + scaler_file_extension
        model_filename = "ds=sip+s=AAPL+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min+fm=vwap+sm=trade_count+tm=+r=36+sort=False+rfm=False+rsm=False+rtm=False+d=+st=minmax+cts=[0]+Lb=True+e=500+es=True+cb=val_accuracy+p=100+bs=128+tl=0.41606152057647705+ta=0.8365758657455444" + model_file_extension
        model_path = os.path.join(MODELS_BASE_PATH, scaler_name, model_filename)
        scaler_path = os.path.join(DATA_BASE_PATH, scaler_name, scaler_filename)
        return model_path, scaler_path
    elif stock_ID == "MSFT":
        model_filename = "ds=sip+s=MSFT+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min+fm=vwap+sm=trade_count+tm=+r=36+sort=False+rfm=False+rsm=False+rtm=False+d=+st=none+cts=[0]+Lb=True+e=500+es=True+cb=val_accuracy+p=100+bs=128+tl=0.3996354639530182+ta=0.8395842909812927" + model_file_extension
        model_path = os.path.join(MODELS_BASE_PATH, model_filename)
        return model_path, None
    elif stock_ID == "AMZN":
        scaler_name = "Robust"
        scaler_filename = "robust_ds=sip+s=AMZN+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min" + scaler_file_extension
        model_filename = "ds=sip+s=AMZN+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min+fm=vwap+sm=trade_count+tm=+r=36+sort=False+rfm=False+rsm=False+rtm=False+d=+st=robust+cts=[0]+Lb=True+e=500+es=True+cb=val_accuracy+p=100+bs=128+tl=0.475951611995697+ta=0.8117924332618713" + model_file_extension
        model_path = os.path.join(MODELS_BASE_PATH, scaler_name, model_filename)
        scaler_path = os.path.join(DATA_BASE_PATH, scaler_name, scaler_filename)
        return model_path, scaler_path
    elif stock_ID == "GOOG":
        scaler_name = "Robust"
        scaler_filename = "robust_ds=sip+s=GOOG+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min" + scaler_file_extension
        model_filename = "ds=sip+s=GOOG+mp=False+sd=2016-01-1+ed=2024-12-30+tf=5Min+fm=vwap+sm=trade_count+tm=+r=36+sort=False+rfm=False+rsm=False+rtm=False+d=+st=robust+cts=[0]+Lb=True+e=500+es=True+cb=val_accuracy+p=100+bs=128+tl=0.539172351360321+ta=0.813238799571991" + model_file_extension
        model_path = os.path.join(MODELS_BASE_PATH, scaler_name, model_filename)
        scaler_path = os.path.join(DATA_BASE_PATH, scaler_name, scaler_filename)
        return model_path, scaler_path
    else:
        raise ValueError(f"Unsupported stock ID: {stock_ID}")

    return None, None
# import pandas as pd


def main_model_stats():
    st.header("Model Stats")
    # Placeholder for data source selection if needed later
    data_source = "IEX"  # Example, could be made dynamic
    scaler_type = "MinMax"  # Example, could be made dynamic

    stocks = ["NVDA", "AAPL", "MSFT", "AMZN", "GOOG", "VOO", "DIA", "IWM"]
    selected_stock = st.selectbox("Select Stock/ETF:", stocks)

    if selected_stock:
        st.subheader(f"Performance Metrics for {selected_stock}")

        # --- Dummy Paths and Values ---
        # Replace these with actual logic to find the correct files/values
        dummy_image_path_template = f"Simons/Images/{data_source}/{selected_stock}_{{type}}.png"  # Placeholder
        dummy_metrics_file_path = f"Models/{data_source}/{scaler_type}/ds={data_source.lower()}+s={selected_stock}+...json"  # Placeholder
        dummy_test_accuracy = 0.75  # Placeholder
        dummy_test_loss = 0.55  # Placeholder
        # --- End Dummy ---

        # Display Metrics
        col1, col2 = st.columns(2)
        with col1:
            st.metric(label="Test Accuracy", value=f"{dummy_test_accuracy:.4f}")
        with col2:
            st.metric(label="Test Loss", value=f"{dummy_test_loss:.4f}")

        st.divider()

        # Display Images
        st.subheader("Model Training History & Evaluation")
        loss_curve_path = dummy_image_path_template.format(type="loss_curve")
        accuracy_curve_path = dummy_image_path_template.format(type="accuracy_curve")
        confusion_matrix_path = dummy_image_path_template.format(type="confusion_matrix")

        # Check if images exist before displaying (optional but good practice)
        # For now, we assume they exist with dummy paths
        st.image(loss_curve_path, caption=f"{selected_stock} Loss Curve", use_column_width=True)
        st.image(accuracy_curve_path, caption=f"{selected_stock} Accuracy Curve", use_column_width=True)
        st.image(confusion_matrix_path, caption=f"{selected_stock} Confusion Matrix", use_column_width=True)

        # Placeholder for future logic to load actual metrics from JSON
        # try:
        #     # Find the correct JSON file based on selected_stock, data_source, scaler_type
        #     # This requires parsing filenames or having a manifest
        #     # Example: find file matching f"Models/{data_source}/{scaler_type}/ds={data_source.lower()}+s={selected_stock}*+ta=*.json"
        #     # with open(actual_metrics_file_path, 'r') as f:
        #     #     # Assuming filename contains metrics or file content does
        #     #     # Extract actual_test_accuracy and actual_test_loss
        #     pass  # Replace with actual loading logic
        # except FileNotFoundError:
        #     st.error(f"Metrics file not found for {selected_stock}.")
        # except Exception as e:
        #     st.error(f"Error loading metrics: {e}")

# If running this script directly (optional)
# if __name__ == "__main__":
#     main_model_stats()
