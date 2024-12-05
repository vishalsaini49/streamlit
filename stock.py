import yfinance as yf
import streamlit as st
import datetime as dt

stock = 'MSFT'
ticker_df = yf.Ticker(stock)
col1, col2 = st.columns(2)

with col1:
    start_date = st.date_input(f"{st.header("Select Start Date")}", dt.date(year=2023, month=1, day=1))
with col2:
    end_date = st.date_input("Select End Date", dt.date.today())

hist = ticker_df.history(period='1d', start=start_date, end=end_date)

st.dataframe(hist)
st.write(hist)