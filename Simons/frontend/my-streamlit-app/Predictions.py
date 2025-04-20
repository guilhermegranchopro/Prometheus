import streamlit as st
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model
import joblib
import alpaca_trade_api as tradeapi
import os
import pandas as pd

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../..'))
MODELS_BASE_PATH = os.path.join(BASE_DIR, "Models/SIP")
DATA_BASE_PATH = os.path.join(BASE_DIR, "Data/SIP/Scalers")

def get_paths(stock_ID):
   model_filename = f"model_{stock_ID}.h5"
   scaler_filename = f"scaler_{stock_ID}.pkl"

   model_path = os.path.join(MODELS_BASE_PATH, "Standard", model_filename)
   scaler_path = os.path.join(DATA_BASE_PATH, "Standard", scaler_filename)

   if not os.path.exists(model_path):
       raise FileNotFoundError(f"Model file not found at {model_path}")
   if not os.path.exists(scaler_path):
       raise FileNotFoundError(f"Scaler file not found at {scaler_path}")

   return model_path, scaler_path

def get_data(stock_ID):
   API_KEY = os.getenv('ALPACA_API_KEY', 'YOUR_API_KEY')
   SECRET_KEY = os.getenv('ALPACA_SECRET_KEY', 'YOUR_SECRET_KEY')
   BASE_URL = 'https://paper-api.alpaca.markets'

   if API_KEY == 'YOUR_API_KEY' or SECRET_KEY == 'YOUR_SECRET_KEY':
       st.error("Please set your Alpaca API Key and Secret Key.")
       return None

   api = tradeapi.REST(key_id=API_KEY, secret_key=SECRET_KEY, base_url=BASE_URL)

   try:
      from alpaca_trade_api.rest import TimeFrame
      import datetime
      end_date = datetime.datetime.now()
      start_date = end_date - datetime.timedelta(days=90)

      data = api.get_bars(stock_ID, TimeFrame.Day, start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d')).df
      if data.empty:
          st.warning(f"No data received from Alpaca for {stock_ID}.")
          return None
      data = data.sort_index()
      return data
   except Exception as e:
      st.error(f"Error fetching data from Alpaca for {stock_ID}: {e}")
      return None

def get_predictions(stock_ID):
   try:
      model_path, scaler_path = get_paths(stock_ID)
   except FileNotFoundError as e:
      st.error(f"Configuration error: {e}")
      return None, None

   try:
      scaler = joblib.load(scaler_path)
   except Exception as e:
      st.error(f"Error loading scaler from {scaler_path}: {e}")
      return None, None

   try:
      model = load_model(model_path)
   except Exception as e:
      st.error(f"Error loading model from {model_path}: {e}")
      return None, None

   data_df = get_data(stock_ID)
   if data_df is None:
      return None, data_df

   features = ['open', 'high', 'low', 'close', 'volume']
   if not all(feature in data_df.columns for feature in features):
       st.error(f"Required features ({features}) not found in Alpaca data columns: {data_df.columns.tolist()}")
       return None, data_df

   data_features = data_df[features]
   data_features = data_features.fillna(method='ffill').fillna(method='bfill')
   if data_features.isnull().values.any():
       st.warning("NaN values remain after fillna, prediction might be unreliable.")

   if data_features.empty:
       st.error("No valid data available for scaling after preprocessing.")
       return None, data_df

   try:
      scaled_data = scaler.transform(data_features)
   except Exception as e:
      st.error(f"Error scaling data: {e}")
      return None, data_df

   if scaled_data.shape[0] > 0:
       latest_scaled_data = scaled_data[-1].reshape(1, -1)

       try:
           predictions = model.predict(latest_scaled_data)
           return predictions, data_df
       except Exception as e:
           st.error(f"Error during model prediction: {e}")
           return None, data_df
   else:
       st.error("Scaled data is empty, cannot make prediction.")
       return None, data_df

def main_predictions():
    st.header("Predictions")
    stocks = ["NVDA", "AAPL", "MSFT", "AMZN", "GOOG", "VOO", "DIA", "IWM"]
    selected_stock = st.selectbox("Select Stock/ETF:", stocks)

    if selected_stock:
        st.info(f"Fetching data and generating prediction for {selected_stock}...")
        predictions, data_df = get_predictions(selected_stock)

        if predictions is not None and data_df is not None:
            latest_prediction = predictions[0][0]

            try:
                num_features = len(['open', 'high', 'low', 'close', 'volume'])
                dummy_row = scaled_data[-1].copy()
                prediction_feature_index = ['open', 'high', 'low', 'close', 'volume'].index('close')
                dummy_row[prediction_feature_index] = latest_prediction

                inverse_transformed_row = scaler.inverse_transform(dummy_row.reshape(1, -1))
                predicted_price = inverse_transformed_row[0, prediction_feature_index]

                last_actual_close = data_df['close'].iloc[-1]
                delta = predicted_price - last_actual_close

                st.metric(
                    label=f"Predicted Next Close Price for {selected_stock}",
                    value=f"${predicted_price:.2f}",
                    delta=f"{delta:.2f} ({delta/last_actual_close:.2%}) vs last close"
                )
                st.write(f"Last actual close price: ${last_actual_close:.2f}")

            except Exception as e:
                st.warning(f"Could not inverse transform prediction. Displaying raw value. Error: {e}")
                st.metric(label=f"Raw Predicted Value for {selected_stock}", value=f"{latest_prediction:.4f}")
                st.write("Note: This value might be scaled or represent something other than price.")

            st.subheader("Recent Market Data")
            st.dataframe(data_df.tail())

        elif data_df is None and predictions is None:
            pass
        else:
            st.error(f"Could not generate prediction for {selected_stock}, but data was fetched.")
            if data_df is not None:
                st.subheader("Recent Market Data (Prediction Failed)")
                st.dataframe(data_df.tail())
