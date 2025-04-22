import streamlit as st
import tensorflow as tf
import joblib
import alpaca_trade_api as tradeapi
import os
from alpaca_trade_api.rest import TimeFrame
import datetime

def get_paths(stock_ID):
   BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
   MODELS_BASE_PATH = os.path.join(BASE_DIR, "Models/SIP")
   DATA_BASE_PATH = os.path.join(BASE_DIR, "Data/SIP/Scalers")

   model_file_extension = ".h5"
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

def get_data(stock_ID):
   API_KEY = os.getenv('ALPACA_API_KEY')
   SECRET_KEY = os.getenv('ALPACA_SECRET_KEY')
   BASE_URL = 'https://api.alpaca.markets'

   if API_KEY is None or SECRET_KEY is None:
       st.error("Please set your Alpaca API Key and Alpaca Secret Key.")
       return None

   api = tradeapi.REST(key_id=API_KEY, secret_key=SECRET_KEY, base_url=BASE_URL)

   end_date = datetime.datetime.now()
   start_date = end_date - datetime.timedelta(days=90)

   data = api.get_bars(stock_ID, TimeFrame.Day, start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d')).df
   if data.empty:
       st.warning(f"No data received from Alpaca for {stock_ID}.")
       return None
   data = data.sort_index()
   return data


def get_predictions(stock_ID):
   model_path, scaler_path = get_paths(stock_ID)

   # Load scaler if available
   if scaler_path:
       scaler = joblib.load(scaler_path)
   else:
       scaler = None

   model = tf.keras.models.load_model(model_path)

   data_df = get_data(stock_ID)
   if data_df is None:
      return None, None, scaler, None

   features = ['vwap', 'trade_count']
   if not all(feature in data_df.columns for feature in features):
       st.error(f"Required features ({features}) not found in Alpaca data columns: {data_df.columns.tolist()}")
       return None, data_df, scaler, None

   data_features = data_df[features]
   data_features = data_features.fillna(method='ffill').fillna(method='bfill')
   if data_features.isnull().values.any():
       st.warning("NaN values remain after fillna, prediction might be unreliable.")

   if data_features.empty:
       st.error("No valid data available for scaling after preprocessing.")
       return None, data_df, scaler, None

   # Scale or use raw data depending on scaler availability
   if scaler:
       scaled_data = scaler.transform(data_features)
   else:
       scaled_data = data_features.values

   if scaled_data is not None and scaled_data.shape[0] > 0:
       latest_scaled_data = scaled_data[-1].reshape(1, -1)

       predictions = model.predict(latest_scaled_data)
       return predictions, data_df, scaler, scaled_data
   else:
       st.error("Scaled data is empty or invalid, cannot make prediction.")
       return None, data_df, scaler, scaled_data


def main_predictions():
    st.header("Predictions")
    stocks = ["NVDA", "AAPL", "MSFT", "AMZN", "GOOG", "VOO", "DIA", "IWM"]
    selected_stock = st.selectbox("Select Stock/ETF:", stocks)

    if selected_stock:
        st.info(f"Fetching data and generating prediction for {selected_stock}...")
        predictions, data_df, scaler, scaled_data = get_predictions(selected_stock)

        if predictions is not None and data_df is not None and scaler is not None and scaled_data is not None:
            latest_prediction = predictions[0][0]

            st.metric(label=f"Raw Predicted Value for {selected_stock}", value=f"{latest_prediction:.4f}")
            st.write("Note: This value might be scaled or represent something other than price. Inverse transform logic needs review based on scaler features.")

            last_actual_close = data_df['close'].iloc[-1]
            st.write(f"Last actual close price: ${last_actual_close:.2f}")

            st.subheader("Recent Market Data Used for Prediction")
            st.dataframe(data_df.tail())

        elif data_df is None and predictions is None:
            st.warning(f"Could not fetch data for {selected_stock}.")
        else:
            st.error(f"Could not generate prediction for {selected_stock}.")
            if data_df is not None:
                st.subheader("Recent Market Data (Prediction Failed)")
                st.dataframe(data_df.tail())

if __name__ == '__main__':
    main_predictions()
