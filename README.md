# Title
To Invest or To Trade?

# About
This project aims to analyze the NASDAQ 100 index and to determine whether it is more profitable to trade in undervalued stocks or to invest in them. This project contains two parts. 

Part 1 <br/>
This part calculates a Robust Value score (RV Score) for each company by percentile ranking of financial ratios. 

This part uses the following financial metrics/ratios: <br/>
stock price, price/earnings, price/book, price/sales, ev/ebitda ev/gross profit

Part 2 <br/>
This part uses market data to calculate the exponential moving averages of the stocks selected in Part 1 to determine the most profitable set of moving averages. The days for the averages included in the analysis are all considered Fibonacci numbers. 

This part uses the following financial metrics: <br/>
open, high, low, close

Streamlit Web App <br/>
TITT (To Invest or To Trade?) web application provides visualization of Part 2's analysis. TITT features current market data, stock charts, and company details and information. Find the most profitable set of moving averages with a few clicks of your mouse. Start by selecting a stock from the menu, a time period, and find out which strategy is best for you.

# Technologies
This analysis was made using Python (v3.7.0), WindowsOS (v20H2), and Jupyter Lab.

Part 1 Libraries <br/>
numpy, pandas, requests, xlsxwriter, math, pathlib (Path), scipy (stats), statistics (mean)

Part 1 APIs <br/>
IEX Cloud (https://iexcloud.io/)

Part 2 Libraries <br/>
os, pandas, dotenv (load_dotenv), matplotlib.pyplot, numpy, pathlib (Path)

Part 2 APIs <br/>
Alpaca (https://alpaca.markets/)

App <br/>
pandas, numpy, yfinance, pathlib, streamlit

# Data
This project uses the aforementioned APIs to pull live data. This project also reads files in CSV  and XLSX format. 

# Usage

Part 1 <br/>
Clone the repository and run the nasdaq_filter.ipynb file.

Part 2 <br/>
Clone the repository and run the moving_averages.ipynb file.

Clone the repository and run the following command in your terminal: streamlit run titt.py. Note: you must run the command in the same directory the program is saved in.

# Contributors
Jacob Honig jacobdhonig@gmail.com www.linkedin.com/jacob-honig/ <br/>
Carl Frederick carljfrederick01@gmail.com www.linkedin.com/in/carl-j-frederick <br/>
Osama Mohamed
