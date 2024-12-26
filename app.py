import streamlit as st
st.set_page_config(
    page_title="Stock Revenue Calculator",
    layout="wide",
    initial_sidebar_state="collapsed",
    page_icon = ":material/calculate:"
)
import pandas as pd
import yfinance as yf
from datetime import datetime, date
import time 
import os
from src import save_text_to_file, calculate_investment_return, compute_total_return

st.logo(image="assets/Full_Logo.png", size='large', icon_image="assets/Small_Logo.png")
st.markdown(
    """
    <style>
    img[data-testid="stLogo"]{
    height:50px;
    width:800;
    }   
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center;'>Stock Revenue Calculator</h1>", unsafe_allow_html=True)
stock_ticker_file = 'Tickers\Stock_Tickers'
stock_tickers = pd.read_csv(stock_ticker_file).squeeze().tolist()

if 'submitted' not in st.session_state:
    st.session_state.submitted = False

with st.form(key='stock_form'):
    selected_ticker = st.selectbox("Select Stock Ticker", stock_tickers, index=16)
    today = date.today()
    col1,col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start date", date(2020, 11, 1), max_value=today)
    with col2:
        end_date = st.date_input("End date", date(2022, 12, 31), max_value=today)
    invested_amount = st.number_input("Invested Amount (in dollars)", min_value=0.0, format="%.2f")
    submit_button = st.form_submit_button(label="Submit", icon=":material/calculate:")

if submit_button and not st.session_state.submitted:
    st.session_state.submitted = True 

if st.session_state.submitted:
    return_rate, final_amount = calculate_investment_return(selected_ticker, start_date, end_date, invested_amount)
    if return_rate is None:
        st.write("Calculation could not be performed as start and end dates are same.")
    else:
        profit_or_loss = final_amount - invested_amount
        if isinstance(profit_or_loss, pd.Series):
            profit_or_loss = profit_or_loss.iloc[0]
        if profit_or_loss >= 0:
            result_color = "green"
            bg_color = "#d4f7d0"
            change_phrase = "appreciated to" 
            result_message = f"Your total profit is ${profit_or_loss:.2f}."
        else:
            result_color = "red"
            bg_color = "#f7b7b7"
            change_phrase = "decreased to"
            result_message = f"Your total loss is ${abs(profit_or_loss):.2f}."
        if isinstance(final_amount, pd.Series):
            final_amount = final_amount.iloc[0]
        with st.container(border=True):
            html_content = f"""
            <h3 style="text-align: center; font-weight: bold; margin-top: 20px;">Investment Result</h3>
            <p style="font-size: 18px; text-align: center; padding: 10px; border-radius: 5px;">
                If you had made an investment of <strong>${invested_amount:.2f}</strong> in <strong>{selected_ticker}</strong> stock between <strong>{start_date}</strong> and <strong>{end_date}</strong>, your investment would have {change_phrase} <strong>${final_amount:.2f}</strong>.
            </p>
            <p style="color: {result_color}; font-size: 18px; font-weight: bold; text-align: center; padding: 10px; border-radius: 5px; background-color: {bg_color};">
                {result_message}
            </p>
            """
            with st.container(border=True):
                st.markdown(html_content, unsafe_allow_html=True)
            html_content_investement = f"""
                <h3 style="text-align: center; font-weight: bold; margin-top: 30px;">Investment Summary</h3>

                <p style="text-align: center;">Below is a summary of your investment calculation:</p>

                <table style="margin: 0 auto; border-collapse: collapse; width: 80%; text-align: left;">
                    <thead>
                        <tr>
                            <th style="padding: 8px; border: 1px solid #ddd; background-color: #f2f2f2;">Stock Ticker</th>
                            <th style="padding: 8px; border: 1px solid #ddd; background-color: #f2f2f2;">Start Date</th>
                            <th style="padding: 8px; border: 1px solid #ddd; background-color: #f2f2f2;">End Date</th>
                            <th style="padding: 8px; border: 1px solid #ddd; background-color: #f2f2f2;">Invested Amount</th>
                            <th style="padding: 8px; border: 1px solid #ddd; background-color: #f2f2f2;">Profit/Loss</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td style="padding: 8px; border: 1px solid #ddd;">{selected_ticker}</td>
                            <td style="padding: 8px; border: 1px solid #ddd;">{start_date}</td>
                            <td style="padding: 8px; border: 1px solid #ddd;">{end_date}</td>
                            <td style="padding: 8px; border: 1px solid #ddd;">${invested_amount:.2f}</td>
                            <td style="padding: 8px; border: 1px solid #ddd; color: {result_color};">{final_amount - invested_amount:.2f}</td>
                        </tr>
                    </tbody>
                </table>            
            """
            with st.container(border=True):
                st.markdown(html_content_investement, unsafe_allow_html=True)

with st.sidebar:
    st.subheader("Add Insights")
    insights_text = st.text_area("Type your insights here", height=200)
    current_time = datetime.now().strftime("%H:%M - %d/%m/%Y")
    insights_text_with_datetime = f"{current_time}\n{insights_text}\n\n"

    if st.button("Save Insights", icon=":material/save:", use_container_width=True):
        save_text_to_file(insights_text_with_datetime)
        st.markdown('<style>div[data-baseweb="toast"] div {color: green;}</style>', unsafe_allow_html=True)
        st.toast('Insights saved successfully!')
        time.sleep(.5)

    if not os.path.exists("Insights.txt"):
        with open("Insights.txt", "w") as file:
            file.write("Stock Data(Insights): \n\n")

    insights = st.button("Show Insights", icon=":material/description:", use_container_width= True)
    
if insights:
    @st.dialog("Insights", width="large")
    def insights():
        if os.path.exists("Insights.txt"):
            with open("Insights.txt", "r") as file:
                insights = file.read()
            st.text_area("Saved Insights", insights, height=300)
        else:
            st.warning("No insights saved yet.")
    insights()
                




















