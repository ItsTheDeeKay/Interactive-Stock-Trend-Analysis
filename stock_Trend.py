# Author: DeeKay Goswami

import sys
import requests
import pandas as pd
import plotly.graph_objects as pltly
from plotly.subplots import make_subplots

# This will define AlphaVantage API Key...
API_KEY = "76XX92VOVAVFF1ID"

# This will define stock symbol, e.g TSLA for Tesla, MSFT for Microsoft...
if len(sys.argv) > 2:
    SYMBOL = sys.argv[1]
    start_Year = sys.argv[2]
else:
    print("Stock symbol or starting year not provided. Using TESLA as default: TSLA 2020")
    SYMBOL = "TSLA"
    start_Year = "2020"

# This will fetch the Weekly Time Series data by calling API..
response = requests.get(f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={SYMBOL}&apikey={API_KEY}')
data = response.json()

# This will print the raw fetched data through API calling...
# print("RAW Data:")
# print(data)

# This will check if the response contains any error message...
if "Error Message" in data:
    print(f"Error: {data['Error Message']}")
    print("Stock SYMBOL INVALID")
    sys.exit(1)
elif "Note" in data:
    print(f"Note: {data['Note']}")
else:
    try:
        # This will extract the 'Weekly Time Series' data from the response, 
                # transpose it to swap rows and columns, and convert it to a pandas DataFrame...
        df = pd.DataFrame(data["Weekly Time Series"]).T

        # This will convert the index to datetime and the data to float...
        df.index = pd.to_datetime(df.index)
        for col in df.columns:
            df[col] = pd.to_numeric(df[col], errors = "coerce")

    except KeyError:
        print("KeyError: The response data does not contain 'Weekly Time Series'. Please check the API key and the stock symbol.")

# This will final print the pre-processed data in dataframe...

# print(df)

# # # # # # # # # # # # # # # # # # # # # # TESLA STOCK or USER PROVIDED STOCK # # # # # # # # # # # # # # # # # # # # # # 

# This will Filter and sort the stock data according to the inputted year...
df_sorted = df.sort_index(ascending = True)
df_Filtered = df_sorted.loc[start_Year:]
print()
print("Stock data fetched successfully.")
print("Plotting graphs...")

# This will calculate moving averages...
short_Rolling = df_Filtered['4. close'].rolling(window = 4).mean()
long_Rolling = df_Filtered['4. close'].rolling(window = 12).mean()

# This will create subplots: candlestick + moving averages, volume...
fig = make_subplots(rows = 2, cols = 1, shared_xaxes = True, 
                    subplot_titles = (f'Weekly Close Prices and Moving Averages for {SYMBOL} ({start_Year} to Present)', 
                                    f'Weekly Trading Volume for {SYMBOL} ({start_Year} to Present)'), 
                    vertical_spacing = 0.3)

# This will add candlestick chart of the stock data...
fig.add_trace(pltly.Candlestick(x = df_Filtered.index, open = df_Filtered['1. open'], high = df_Filtered['2. high'], 
                             low = df_Filtered['3. low'], close = df_Filtered['4. close'], 
                             name  =  'Price'), row = 1, col = 1)

# This will add trace of moving averages...
fig.add_trace(pltly.Scatter(x = short_Rolling.index, y = short_Rolling, 
                         line = dict(color = 'blue', width = 1), name = '4-Weeks Moving Average'), row = 1, col = 1)

fig.add_trace(pltly.Scatter(x = long_Rolling.index, y = long_Rolling, 
                         line = dict(color = 'red', width = 1), name = '12-Weeks Moving Average'), row = 1, col = 1)

# This will plot the volume data...
fig.add_trace(pltly.Bar(x = df_Filtered.index, y = df_Filtered['5. volume'], name = 'Volume'), row = 2, col = 1)

fig.update_layout(height = 800, width = 1000)
fig.show()

# This will ask whether to save plot image or not...
def save():
    save_Image = input("Press [Y] to save plot image or [N] to discard this stock data: ").strip().lower()
    if save_Image == 'y':
        fig.write_image(f"{SYMBOL}_stock_Analysis.png")
        print(f"Image saved as {SYMBOL}_stock_Analysis.png")
    elif save_Image == 'n':
        print("Stock data discarded.")
    else:
        print("Invalid input. Please enter 'Y' or 'N'.")
        save()
save()

# # # # # # # # # # # # # # # # # # # # # # # # END # # # # # # # # # # # # # # # # # # # # # # # 
