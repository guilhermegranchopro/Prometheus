import streamlit as st
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model
import joblib
import alpaca_trade_api as tradeapi


def get_paths(stock_ID):
   model_path = "/Models/SIP"
   scaler_path = "/Data/SIP/Scaler"
   if stock_ID == "NVDA":
      model_path = f"{model_path}/NVDA_model.h5"
      scaler_path = f"{scaler_path}/NVDA_scaler.pkl"
   elif stock_ID == "AAPL":
      model_path = f"{model_path}/AAPL_model.h5"
      scaler_path = f"{scaler_path}/AAPL_scaler.pkl"
   elif stock_ID == "MSFT":
      model_path = f"{model_path}/MSFT_model.h5"
      scaler_path = f"{scaler_path}/MSFT_scaler.pkl"
   elif stock_ID == "AMZN":
      model_path = f"{model_path}/AMZN_model.h5"
      scaler_path = f"{scaler_path}/AMZN_scaler.pkl"
   elif stock_ID == "GOOG":
      model_path = f"{model_path}/GOOG_model.h5"
      scaler_path = f"{scaler_path}/GOOG_scaler.pkl"
   elif stock_ID == "VOO":
      model_path = f"{model_path}/VOO_model.h5"
      scaler_path = f"{scaler_path}/VOO_scaler.pkl"
   elif stock_ID == "DIA":
      model_path = f"{model_path}/DIA_model.h5"
      scaler_path = f"{scaler_path}/DIA_scaler.pkl"
   elif stock_ID == "IWM":
      model_path = f"{model_path}/IWM_model.h5"
      scaler_path = f"{scaler_path}/IWM_scaler.pkl"
   else:
      raise ValueError("Invalid stock ID provided.")
   
   return model_path, scaler_path

def get_data(stock_ID):

   # Initialize API connection (replace with your actual keys)
   api = tradeapi.REST(
      key_id='YOUR_API_KEY',
      secret_key='YOUR_SECRET_KEY',
      base_url='https://paper-api.alpaca.markets' # Use paper trading endpoint for testing
   )

   # Fetch market data for Apple (AAPL)
   try:
      data = api.get_bars('AAPL', '1D', '2024-01-01', '2024-04-15').df
      # Example: Print the first few rows
      # print(data.head())
   except Exception as e:
      print(f"Error fetching data: {e}") # Use print or logging in actual script

   return data

def get_predictions(stock_ID):
   model_path, scaler_path = get_paths(stock_ID)

   scaler = joblib.load(scaler_path)

   # Load the model
   model = load_model(model_path)

   data = ...

   predictions = model.predict(scaler.transform(data))

   return predictions

def main_predictions():
    st.header("Predictions")
    # Stock Selection - Moved inside the Model Stats tab
    stocks = ["NVDA", "AAPL", "MSFT", "AMZN", "GOOG", "VOO", "DIA", "IWM"]
    selected_stock = st.selectbox("Select Stock/ETF:", stocks)
    get_predictions(selected_stock)
    # Display the selected stock
    st.write(
        f"Detailed statistics and prediction visualization for {selected_stock} will go here."
    )
