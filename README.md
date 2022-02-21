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
TITT (To Invest or To Trade?) web application provides additional visualization of Part 2's analysis. TITT features current market data, stock charts, and company details and information. Find the most profitable set of moving averages with a few clicks of your mouse. Start by selecting a stock from the menu, a time period, and evaluate the strategy for each stock.

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
When using this program, upload the list of NASDAQ stocks in the following format:

![Screen Shot 2022-02-20 at 6 10 19 PM](https://user-images.githubusercontent.com/95586624/154868524-2edb77b1-0b9f-4dc8-9206-783d8f4a1973.png)


Part 2 <br/>
When using this report, upload the filtered list of undervalued stocks from part 1 in the following format:

![Screen Shot 2022-02-20 at 5 59 37 PM](https://user-images.githubusercontent.com/95586624/154868184-b6b7bd85-aeab-42c3-9e3c-5938ce2de161.png)

Streamlit App
Open terminal, navigate to the project_1 directory, and run titt.py using python: 

![Screen Shot 2022-02-20 at 6 02 56 PM](https://user-images.githubusercontent.com/95586624/154868278-858d648c-e6b1-43d8-98de-53c9a9db1ea1.png)


# Contributors
Jacob Honig jacobdhonig@gmail.com www.linkedin.com/jacob-honig/ <br/>
Carl Frederick carljfrederick01@gmail.com www.linkedin.com/in/carl-j-frederick <br/>
Osama Mohamed osamahuss8@icloud.com
