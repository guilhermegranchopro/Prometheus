import streamlit as st
import os

def get_paths(stock_ID):
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    IMAGES_BASE_PATH = os.path.join(BASE_DIR, "Simons/Images/SIP")

    images_file_extension = ".png"

    if stock_ID == "VOO":
        accuracy_curve_filename = "VOO_sip_noscaler_accuracy" + images_file_extension
        loss_curve_filename = "VOO_sip_noscaler_loss" + images_file_extension
        confusion_matrix_filename = "VOO_sip_noscaler_cm" + images_file_extension
        accuracy_curve_path = os.path.join(IMAGES_BASE_PATH, "NoScaler", "VOO", accuracy_curve_filename)
        loss_curve_path = os.path.join(IMAGES_BASE_PATH, "NoScaler", "VOO", loss_curve_filename)
        confusion_matrix_path = os.path.join(IMAGES_BASE_PATH, "NoScaler", "VOO", confusion_matrix_filename)
        test_accuracy = 0.8780
        test_loss = 0.3060
        return accuracy_curve_path, loss_curve_path, confusion_matrix_path, test_accuracy, test_loss
    elif stock_ID == "DIA":
        accuracy_curve_filename = "DIA_sip_noscaler_accuracy" + images_file_extension
        loss_curve_filename = "DIA_sip_noscaler_loss" + images_file_extension
        confusion_matrix_filename = "DIA_sip_noscaler_cm" + images_file_extension
        accuracy_curve_path = os.path.join(IMAGES_BASE_PATH, "NoScaler", "DIA", accuracy_curve_filename)
        loss_curve_path = os.path.join(IMAGES_BASE_PATH, "NoScaler", "DIA", loss_curve_filename)
        confusion_matrix_path = os.path.join(IMAGES_BASE_PATH, "NoScaler", "DIA", confusion_matrix_filename)
        test_accuracy = 0.8420
        test_loss = 0.3770
        return accuracy_curve_path, loss_curve_path, confusion_matrix_path, test_accuracy, test_loss
    elif stock_ID == "IWM":
        accuracy_curve_filename = "IWM_sip_noscaler_accuracy" + images_file_extension
        loss_curve_filename = "IWM_sip_noscaler_loss" + images_file_extension
        confusion_matrix_filename = "IWM_sip_noscaler_cm" + images_file_extension
        accuracy_curve_path = os.path.join(IMAGES_BASE_PATH, "NoScaler", "IWM", accuracy_curve_filename)
        loss_curve_path = os.path.join(IMAGES_BASE_PATH, "NoScaler", "IWM", loss_curve_filename)
        confusion_matrix_path = os.path.join(IMAGES_BASE_PATH, "NoScaler", "IWM", confusion_matrix_filename)
        test_accuracy = 0.8340
        test_loss = 0.3770
        return accuracy_curve_path, loss_curve_path, confusion_matrix_path, test_accuracy, test_loss
    elif stock_ID == "NVDA":
        accuracy_curve_filename = "NVDA_sip_robust_accuracy" + images_file_extension
        loss_curve_filename = "NVDA_sip_robust_loss" + images_file_extension
        confusion_matrix_filename = "NVDA_sip_robust_cm" + images_file_extension
        accuracy_curve_path = os.path.join(IMAGES_BASE_PATH, "Robust", "NVDA", accuracy_curve_filename)
        loss_curve_path = os.path.join(IMAGES_BASE_PATH, "Robust", "NVDA", loss_curve_filename)
        confusion_matrix_path = os.path.join(IMAGES_BASE_PATH, "Robust", "NVDA", confusion_matrix_filename)
        test_accuracy = 0.7820
        test_loss = 0.5880
        return accuracy_curve_path, loss_curve_path, confusion_matrix_path, test_accuracy, test_loss
    elif stock_ID == "AAPL":
        accuracy_curve_filename = "AAPL_sip_minmax_accuracy" + images_file_extension
        loss_curve_filename = "AAPL_sip_minmax_loss" + images_file_extension
        confusion_matrix_filename = "AAPL_sip_minmax_cm" + images_file_extension
        accuracy_curve_path = os.path.join(IMAGES_BASE_PATH, "MinMax", "AAPL", accuracy_curve_filename)
        loss_curve_path = os.path.join(IMAGES_BASE_PATH, "MinMax", "AAPL", loss_curve_filename)
        confusion_matrix_path = os.path.join(IMAGES_BASE_PATH, "MinMax", "AAPL", confusion_matrix_filename)
        test_accuracy = 0.8250
        test_loss = 0.4370
        return accuracy_curve_path, loss_curve_path, confusion_matrix_path, test_accuracy, test_loss
    elif stock_ID == "MSFT":
        accuracy_curve_filename = "MSFT_sip_noscaler_accuracy" + images_file_extension
        loss_curve_filename = "MSFT_sip_noscaler_loss" + images_file_extension
        confusion_matrix_filename = "MSFT_sip_noscaler_cm" + images_file_extension
        accuracy_curve_path = os.path.join(IMAGES_BASE_PATH, "NoScaler", "MSFT", accuracy_curve_filename)
        loss_curve_path = os.path.join(IMAGES_BASE_PATH, "NoScaler", "MSFT", loss_curve_filename)
        confusion_matrix_path = os.path.join(IMAGES_BASE_PATH, "NoScaler", "MSFT", confusion_matrix_filename)
        test_accuracy = 0.8610
        test_loss = 0.3770
        return accuracy_curve_path, loss_curve_path, confusion_matrix_path, test_accuracy, test_loss
    elif stock_ID == "AMZN":
        accuracy_curve_filename = "AMZN_sip_robust_accuracy" + images_file_extension
        loss_curve_filename = "AMZN_sip_robust_loss" + images_file_extension
        confusion_matrix_filename = "AMZN_sip_robust_cm" + images_file_extension
        accuracy_curve_path = os.path.join(IMAGES_BASE_PATH, "Robust", "AMZN", accuracy_curve_filename)
        loss_curve_path = os.path.join(IMAGES_BASE_PATH, "Robust", "AMZN", loss_curve_filename)
        confusion_matrix_path = os.path.join(IMAGES_BASE_PATH, "Robust", "AMZN", confusion_matrix_filename)
        test_accuracy = 0.8070
        test_loss = 0.4600
        return accuracy_curve_path, loss_curve_path, confusion_matrix_path, test_accuracy, test_loss
    elif stock_ID == "GOOG":
        accuracy_curve_filename = "GOOG_sip_robust_accuracy" + images_file_extension
        loss_curve_filename = "GOOG_sip_robust_loss" + images_file_extension
        confusion_matrix_filename = "GOOG_sip_robust_cm" + images_file_extension
        accuracy_curve_path = os.path.join(IMAGES_BASE_PATH, "Robust", "GOOG", accuracy_curve_filename)
        loss_curve_path = os.path.join(IMAGES_BASE_PATH, "Robust", "GOOG", loss_curve_filename)
        confusion_matrix_path = os.path.join(IMAGES_BASE_PATH, "Robust", "GOOG", confusion_matrix_filename)
        test_accuracy = 0.8160
        test_loss = 0.5820
        return accuracy_curve_path, loss_curve_path, confusion_matrix_path, test_accuracy, test_loss
    else:
        raise ValueError(f"Unsupported stock ID: {stock_ID}")

    return None, None, None, None, None

# Streamlit app for displaying model statistics
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
