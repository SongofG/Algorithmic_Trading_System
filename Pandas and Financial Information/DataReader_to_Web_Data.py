# Use pandas_datareader package to collect web data.
# Use matplotlib to draw a graph of the stock data

import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt

start = datetime.datetime(2016, 2, 19)  # Year, Month, Day
end = datetime.datetime(2016, 3, 4)

# gs = web.DataReader("078930.KS", "yahoo", start, end)
# gs = web.DataReader("078930", "naver", start, end)  # The same as above.
# print(gs)
# print(gs.info())  # 10 data in total.

gs = web.DataReader("078930.KS", "yahoo")  # Start = 2016/08/16 ~ today.
print(gs.info())  # 1223 data in total

# plt.plot(gs['Adj Close'])  # This is without the date information on the X-axis
# plt.show()

plt.plot(gs.index, gs['Adj Close'])
plt.show()


