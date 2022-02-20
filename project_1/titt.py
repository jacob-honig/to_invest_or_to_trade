# Import the required libraries and dependencies
import pandas as pd
import numpy as np
from pathlib import Path
import yfinance as yf
import streamlit as st

# Uses Path to read in 20 undervalued stocks from value_stratgey csv 
csvpath = Path("./Resources/value_strat.xlsx")
tickers_df = pd.read_excel(csvpath)

# Converts Ticker column in tickers_dataframe to a list
tickers = tickers_df["Ticker"].values.tolist()

# Adds "Select Ticker" to list
#tickers.insert(0, "Select Ticker")

# Creates app title
st.title("TITT")

# Create caption for app description
st.caption("""TITT (To Invest or To Trade?) web application
takes the 20 most undervalued stocks in the NASDAQ Composite and evaluates each 
stock to determine the most profitable set of moving averages. 
TUAC features current market data, stock charts, and company details and information. 
Find cumulative return and exponential moving average results with a few clicks of your mouse. 
Start by selecting a stock from the menu, a time period, and evaluate the strategy for each stock.""")

# Creates sidebar 
st.sidebar.header("Menu")

# Creates ticker picker from sidebar
ticker_dropdown = st.sidebar.selectbox("Stock Symbol", tickers)

# Creates start and end date picker subheader
start_date = st.sidebar.date_input("Start Date", pd.to_datetime("2017-02-01"))
end_date = st.sidebar.date_input("End Date", pd.to_datetime("today"))

# Retrieves ticker data 
ticker_data = yf.Ticker(ticker_dropdown)
stock = ticker_data.history(period  = '1D', start = start_date, end = end_date)

# Creates company name, sector, industry, and summary information
ticker_name = ticker_data.info['longName']
st.header('**%s**' % ticker_name)
logo = '<img src=%s>' % ticker_data.info['logo_url']
st.markdown(logo, unsafe_allow_html=True)
ticker_sector = ticker_data.info['sector']
st.info(ticker_sector)
ticker_industry = ticker_data.info['industry']
st.info(ticker_industry)
ticker_summary = ticker_data.info['longBusinessSummary']
st.info(ticker_summary)

# Creates DataFrame for tickers in the drop down list
st.header('**Market Data**')
st.write(stock)

# Creates Title Chart 
st.header('**Chart**')

# Creates a line chart for all tickers in the drop down
chart = ticker_data.history(period  = '1D', start = start_date, end = end_date)['Close']
st.line_chart(chart)


# Calculates moving averages and returns of selected stock
stock['return'] = stock['Close'].pct_change()
stock['cumulative_return'] = (stock['return'] + 1).cumprod() - 1
stock['2_dayma'] = stock['Close'].ewm(span=2, adjust = False).mean()
stock['3_dayma'] = stock['Close'].ewm(span=3, adjust = False).mean()
stock['5_dayma'] = stock['Close'].ewm(span=5, adjust = False).mean()
stock['8_dayma'] = stock['Close'].ewm(span=8, adjust = False).mean()
stock['13_dayma'] = stock['Close'].ewm(span=13, adjust = False).mean()
stock['21_dayma'] = stock['Close'].ewm(span=21, adjust = False).mean()
stock['34_dayma'] = stock['Close'].ewm(span=34, adjust = False).mean()
stock['55_dayma'] = stock['Close'].ewm(span=55, adjust = False).mean()
stock['strat1_return'] = ''
stock['strat2_return'] = ''
stock['strat3_return'] = ''
stock['strat4_return'] = ''
stock['strat5_return'] = ''
stock['strat6_return'] = ''
stock['strat7_return'] = ''

# Removes missing values 
stock = stock.dropna()

# Sets the conditions for when to enter the position
stock['strat1_return'] = np.where(((stock['Close'] > stock['2_dayma']) & (stock['Close'] > stock['3_dayma'])) | ((stock['Close'] < stock['2_dayma']) & (stock['Close'] < stock['3_dayma'])), stock['return'], 0)
stock['strat2_return'] = np.where(((stock['2_dayma'] > stock['3_dayma']) & (stock['2_dayma'] > stock['5_dayma'])) | ((stock['2_dayma'] < stock['3_dayma']) & (stock['2_dayma'] < stock['5_dayma'])), stock['return'], 0)
stock['strat3_return'] = np.where(((stock['3_dayma'] > stock['5_dayma']) & (stock['3_dayma'] > stock['8_dayma'])) | ((stock['3_dayma'] < stock['5_dayma']) & (stock['3_dayma'] < stock['8_dayma'])), stock['return'], 0)
stock['strat4_return'] = np.where(((stock['5_dayma'] > stock['8_dayma']) & (stock['5_dayma'] > stock['13_dayma'])) | ((stock['5_dayma'] < stock['8_dayma']) & (stock['5_dayma'] < stock['13_dayma'])), stock['return'], 0)
stock['strat5_return'] = np.where(((stock['8_dayma'] > stock['13_dayma']) & (stock['8_dayma'] > stock['21_dayma'])) | ((stock['8_dayma'] < stock['13_dayma']) & (stock['8_dayma'] < stock['21_dayma'])), stock['return'], 0)
stock['strat6_return'] = np.where(((stock['13_dayma'] > stock['21_dayma']) & (stock['13_dayma'] > stock['34_dayma'])) | ((stock['13_dayma'] < stock['21_dayma']) & (stock['13_dayma'] < stock['34_dayma'])), stock['return'], 0)
stock['strat7_return'] = np.where(((stock['21_dayma'] > stock['34_dayma']) & (stock['21_dayma'] > stock['55_dayma'])) | ((stock['21_dayma'] < stock['34_dayma']) & (stock['21_dayma'] < stock['55_dayma'])), stock['return'], 0)


# Creates header
st.header('**Cumulative Return and EMA Strategies of Selected Stock**')

# Calculates the cumulative return of each strategy and prints the stock DataFrame
stock['strat1_cum_return'] = (stock['strat1_return'] + 1).cumprod() - 1
stock['strat2_cum_return'] = (stock['strat2_return'] + 1).cumprod() - 1
stock['strat3_cum_return'] = (stock['strat3_return'] + 1).cumprod() - 1
stock['strat4_cum_return'] = (stock['strat4_return'] + 1).cumprod() - 1
stock['strat5_cum_return'] = (stock['strat5_return'] + 1).cumprod() - 1
stock['strat6_cum_return'] = (stock['strat6_return'] + 1).cumprod() - 1
stock['strat7_cum_return'] = (stock['strat7_return'] + 1).cumprod() - 1

st.write(stock)



# Creates header and line chart for cumlative return and ema strategies of selected stock
stock_dataframe = stock[["cumulative_return", "strat1_cum_return", "strat2_cum_return", "strat3_cum_return", "strat4_cum_return", "strat5_cum_return", "strat6_cum_return", "strat7_cum_return"]]
stock_dataframe.rename(columns= {"cumulative_return": "Cumulative Return of Stock", 
                                "strat1_cum_return": "Strategy #1 [1,2,3]",
                                'strat2_cum_return': "Strategy #2 [2,3,5]",
                                'strat3_cum_return': "Strategy #3 [3,5,8]",
                                'strat4_cum_return': "Strategy #4 [5,8,13]",
                                "strat5_cum_return": "Strategy #5 [8,13,21]",
                                "strat6_cum_return": "Strategy #6 [13,21,34]",
                                "strat7_cum_return": "Strategy #7 [21,34,55]"}, 
                                inplace = True)


st.line_chart(stock_dataframe) 