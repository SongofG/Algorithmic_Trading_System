# Notion notes
# MA: Moving Average (Use adjusted closing price to get the MAs).
# Cross: points where 5, 20, 60, and/or 120 days MA lines meet each others.
# Cross is usually, but not certainly, a crucial timing to trade stocks.
# Moving average is one of basic tools to analyze the trend of the market.

import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt

gs = web.DataReader("078930.KS", "yahoo", "2014-01-01", "2016-03-06")
# print(gs.tail())

ma5 = gs['Adj Close'].rolling(window=5).mean()  # This is not right: Holidays included.
# print(type(ma5))  # Series type
# print(ma5.tail(10))

new_gs = gs[gs['Volume'] != 0]  # Get rid of holidays when there were no tradings.
# print(new_gs.tail(5))  # We got rid of 2016-03-01 since it's Korean National Holiday.

ma5 = new_gs['Adj Close'].rolling(window=5).mean()  # Right 5 days MAs
new_gs.insert(len(new_gs.columns), "MA5", ma5)  # .insert(index of the inserting column, column name, data)
# print(new_gs.tail(5))

# Repeat the procedures above to get MA20, MA60, MA120
ma20 = new_gs['Adj Close'].rolling(window=20).mean()
ma60 = new_gs['Adj Close'].rolling(window=60).mean()
ma120 = new_gs['Adj Close'].rolling(window=120).mean()

new_gs.insert(len(new_gs.columns), "MA20", ma20)
new_gs.insert(len(new_gs.columns), "MA60", ma60)
new_gs.insert(len(new_gs.columns), "MA120", ma120)

# print(new_gs.tail(10))  # Check Result

# Now, we draw the MAs.

plt.plot(new_gs.index, new_gs['Adj Close'], label="Adj Close")  # Draw the adj close line
plt.plot(new_gs.index, new_gs['MA5'], label="MA5")  # Draw the MA5 line
plt.plot(new_gs.index, new_gs['MA20'], label="MA20")  # Draw the MA20 line
plt.plot(new_gs.index, new_gs["MA60"], label="MA60")  # Draw the MA60 line
plt.plot(new_gs.index, new_gs["MA120"], label="MA120")  # Draw the MA120 line
plt.legend(loc="best")  # Automatically locates the legends' explanations.
plt.grid()  # Add grids to the plot.
plt.show()
