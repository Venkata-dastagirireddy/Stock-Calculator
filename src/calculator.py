import streamlit as st
import yfinance as yf

def calculate_investment_return(ticker_symbol, start_date, end_date, invested_amount):
    stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)
    if stock_data.empty:
        return None, None
    closing_prices = stock_data['Close']
    if len(closing_prices) < 2:
        st.error("Not enough data to calculate returns. Please choose a different date range.")
        return None, None
    initial_price = closing_prices.iloc[0]
    final_price = closing_prices.iloc[-1]
    return_rate, final_amount = compute_total_return(initial_price, final_price, invested_amount)
    return return_rate, final_amount

def compute_total_return(initial_price, final_price, initial_investment):
    return_rate = (final_price / initial_price) - 1
    final_amount = initial_investment * (1 + return_rate)
    return return_rate, final_amount