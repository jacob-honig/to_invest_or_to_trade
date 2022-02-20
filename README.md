# Title
To Invest or To Trade?

# About
This project aims to analyze the NASDAQ 100 index and to determine whether it is more profitable to trade in undervalued stocks or invest in them. This project contains two parts. 

Part 1
This part calculates a Robust Value score (RV Score) for each company by percentile ranking of financial ratios. 

This part uses the following financial metrics/ratios:
stock price, price/earnings, price/book, price/sales, ev/ebitda ev/gross profit

Part 2
This part uses market data to calculate the exponential moving averages of the stocks selected in Part 1 to determine the most profitable set of moving averages. The days for the averages included in the analysis are all considered Fibonacci numbers. 

This part uses the following financial metrics:
open, high, low, close


# Technologies
This analysis was made using Python (v3.7.0), WindowsOS (v20H2), and Jupyter Lab.

Part 1 Libraries
numpy, pandas, requests, xlsxwriter, math, pathlib (Path), scipy (stats), statistics (mean)

Part 1 APIs
IEX Cloud (https://iexcloud.io/)

Part 2 Libraries
os, pandas, dotenv (load_dotenv), matplotlib.pyplot, numpy, pathlib (Path)

Part 2 APIs
Alpaca (https://alpaca.markets/)

# Data

# Usage
