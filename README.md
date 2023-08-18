# Interactive Stock Trend Analysis

Authors:  **DeeKay Goswami**

YouTube Video:  [Link](https://youtu.be/HzmqWJ_XQ2s)

---

**NOTE**:  The *italicized* content below is for your reference only.  Please remove these comments before submitting.


---
## Task List
*The table below will serve as your Progress Report (due by end of day on Monday, May 8).  Be sure to list all tasks that you need to complete to finish your analysis and to successfully complete the requirements of this project.*

| ID | Task Description | Due Date | Status |
| --- | --- | --- | --- |
| 1 | Created API Key | 2023-04-30 | DONE |
| 2 | Weekly Time Series Stock data fetched | 2023-05-01 | DONE |
| 3 | Data Pre-processing | 2023-05-03 | DONE |
| 4 | Dataframe parsing| 2023-05-04 | DONE |
| 5 | Moving averages calculation | 2023-05-07 | DONE |
| 6 | Creating plots for visualization | 2023-05-08 | DONE |
| 7 | Final data visualization | 2023-05-08 | DONE |
| 8 | Complete YouTube video and upload to YouTube | 2023-05-16 | DONE |
| 9 | Upload README.md document to Github | 2023-05-17 | DONE |

--- 

## Introduction
*The purpose of this project is to fetch stock market data using the Alpha Vantage API and conduct a detailed analysis. Using Python and its powerful libraries, we process and visualize the data, focusing on the weekly closing prices, moving averages, and trading volume. This data-driven approach provides clear insights into market trends, assisting in informed decision-making.*

---

## References
*In this section, provide links to your references and data sources.  For example:*
- API Calling from  [Alpha Vantage](https://www.alphavantage.co/documentation/)
- The code retrieves stock data of user inputted stock from [Alpha Vantage](https://www.alphavantage.co/documentation/)
- Source Code for calculating moving averages [LearnDataSci](https://www.learndatasci.com/tutorials/python-finance-part-3-moving-average-trading-strategy/)
- CandleStick and other visualization plots from [PlotLy](https://plotly.com/python/candlestick-charts/)

---

## Requirements
*This project requires the following API Key and Python packages:*
- *API Key - 76XX92VOVAVFF1ID*
- *[Requests](https://pypi.org/project/requests/)*
- *[Kaleido](https://pypi.org/project/kaleido/)*
- *[Pandas](https://pypi.org/project/pandas/)*
- *[PlotLy](https://pypi.org/project/plotly/)*

---

## Explanation of the Code

The code, `stock_Trend.py`, begins by importing necessary Python packages:
```
import sys
import requests
import pandas as pd
import plotly.graph_objects as pltly
from plotly.subplots import make_subplots

```
To install these packages, use below command in your terminal:
```
pip install pandas requests plotly kaleido
```
OR
```
pip install -r requirements.txt
``` 

The “Weekly Time Series” data is then fetched using the Alpha Vantage API Key. Below is the code snippet for that:
```
response = requests.get(f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={SYMBOL}&apikey={API_KEY}')
data = response.json()
		
```
Then it will check the response for any error messages:
```
if "Error Message" in data:
    print(f"Error: {data['Error Message']}")
elif "Note" in data:
    print(f"Note: {data['Note']}")
```
Next, we extract the 'Weekly Time Series' data, transpose it to swap rows and columns, and convert it to a panda DataFrame. The index is converted to datetime, and the data is converted to float:
```
df = pd.DataFrame(data["Weekly Time Series"]).T
df.index = pd.to_datetime(df.index)
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors = "coerce")
```

Finally, we visualize the data.  We save our plot as a `SYMBOL_stock_Analysis.png` image:
```
fig = make_subplots(rows = 2, cols = 1, shared_xaxes = True, 
                    subplot_titles = (f'Weekly Close Prices and Moving Averages for {SYMBOL} (2020 to Present)', 
                                    f'Weekly Trading Volume for {SYMBOL} (2020 to Present)'), 
                    vertical_spacing = 0.3)	
fig.update_layout(height = 800, width = 1000)
fig.show()
```

The output from this code is shown below:

![TSLA_stock_Analysis](https://user-images.githubusercontent.com/124843272/236976966-b7755452-e2bc-41a7-9dc0-b15b4929ff35.png)


---

## How to Run the Code
*Provide step-by-step instructions for running the code.  For example, I like to run code from the terminal:*
1. Ensure that you have registered for the Alpha Vantage API key.

2. Ensure that you have installed necessary Python packages: pandas, requests, plotly, and kaleido.

3. Save the stock_Trend.py Python script in your preferred directory.

4. Open a terminal window.

5. Change directories to where `stock_Trend.py` is saved.

6. Type the following command:
	```
	python3 stock_Trend.py AAPL 2015
	```
**You can analyze & visualize almost any stock data (Listed by AlphaVantage) by changing stock symbol and year in above command. If no symbol and year is provided, the code will analyze TESLA's Weekly Time Series from 2020 to present as default.
After plotting, it will ask "Press [Y] to save plot image or [N] to discard this stock data:"**



---

## Results from your Analysis
*The analysis has demonstrated a powerful way to visualize stock market data, making it easier to understand complex financial information. The moving averages provide useful insights into market sentiment, while the trading volume can indicate the level of investor interest and activity in the stock.*

However, there are several potential areas for improvement:

1. Additional Indicators: While moving averages are helpful, they are relatively simple indicators. Incorporating more sophisticated technical indicators like Bollinger Bands, Relative Strength Index (RSI), or Moving Average Convergence Divergence (MACD) could provide more nuanced insights.
2. Sentiment Analysis: Integrating sentiment analysis based on news articles, earnings call transcripts, or social media posts could provide a more holistic view of factors influencing the stock's performance.
3. Comparative Analysis: Comparing the performance of several stocks or comparing a stock against a benchmark index could provide additional context.
4. Predictive Modeling: Implementing machine learning algorithms to predict future price movements could make the analysis more actionable for investment decisions.

This project serves as a solid foundation for more in-depth stock market analysis, and these improvements could greatly enhance its utility.


