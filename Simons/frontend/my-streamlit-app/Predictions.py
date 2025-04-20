import streamlit as st

def main_predictions():
   
   st.header("Predictions")
   # Stock Selection - Moved inside the Model Stats tab
   stocks = ["NVDA", "AAPL", "MSFT", "AMZN", "GOOG", "VOO", "DIA", "IWM"]
   selected_stock = st.selectbox("Select Stock/ETF:", stocks)
   st.write(f"Detailed statistics and prediction visualization for {selected_stock} will go here.")