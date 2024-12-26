# Stock Revenue Calculator

A Streamlit-based web application that allows users to calculate their potential profit or loss from investments in stocks. The app fetches stock data using the `yfinance` library and allows users to input their investment details, including the stock ticker, date range, and invested amount. It then calculates the return on investment (ROI) and provides a summary of the investment performance.

## Features

- **Stock Data Fetching**: Fetches real-time stock data from Yahoo Finance.
- **Investment Return Calculation**: Calculates profit or loss based on user input for a given stock ticker, date range, and invested amount.
- **Result Display**: Displays the result of the investment calculation, including the total profit or loss.
- **Investment Summary**: Provides a detailed table summarizing the investment, including the stock ticker, start date, end date, invested amount, and profit/loss.
- **Insights Storage**: Users can add and save personalized insights about their investment.
- **Responsive Design**: Built with Streamlit for an interactive user experience.

## Cloning This Project

To get started with the **Stock Revenue Calculator** application, you can clone this repository to your local machine.

### Steps to Clone and Run:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
    ```
2. **Install Dependencies**: 
Ensure you have Python installed, and then install the necessary dependencies:

    ```bash
    pip install -r requirements.txt
    ```
3. **Run the Application**: 
Navigate to the project directory and run the Streamlit app:

    ```bash
    streamlit run app.py
    ```
4. **Access the Application**: 
After running the above command, open the provided URL in your browser (usually http://localhost:8501), and you can start using the app.

## Usage

1. **Select Stock Ticker**: Choose a stock ticker from the provided list.
2. **Set Date Range**: Pick the start and end dates for your investment period.
3. **Enter Investment Amount**: Specify how much you invested in the selected stock.
4. **Submit**: Press the "Submit" button to calculate your investment return.
5. **View Results**: The app will display the total profit or loss and an investment summary table.

### Insights Feature

- Users can add personalized insights about their investment and save them for future reference.
- The saved insights are stored in a file, and users can view or modify them as needed.

