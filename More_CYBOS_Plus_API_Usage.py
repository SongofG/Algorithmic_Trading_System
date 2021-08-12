# In Korean stock market, each of the stocks carry unique code.

import win32com.client

# instCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")  # CpCodeMgr class is for getting variety of code info.
# codeList = instCpCodeMgr.GetStockListByMarket(1)  # This returns a tuple of Korean stock market's items
# print(codeList)
#
# # 1. Make a dictionary which has the stock codes as "keys" and the stock names as "values"
# kospi = {}
# for code in codeList:
#     name = instCpCodeMgr.CodeToName(code)
#     kospi[code] = name
#
# # 2. Export the kospi dictionary into a csv file format.
# f = open("C:/Users/박해인/PycharmProjects/Python_Trading/kospi.csv", 'w')  # the second parameter is to "write" a file
# for key, value in kospi.items():
#     f.write("%s, %s\n" % (key, value))
# f.close()
#
# By running the above codes, we can obtain the list of stocks in KOSPI.
# However, just by using the "GetStockListByMarket(1)" method, there are ETFs(Exchange Traded Fund)
# and ETNs(Exchange Traded Note) in the list too.
#
# # 2. Use "GetStockSectionKind" method to distinguish the stocks from other financial goods.
# for i, code in enumerate(codeList):  # Using "enumerate()" method on dict will return the index num and key
#     secondCode = instCpCodeMgr.GetStockSectionKind(code) # Checkout the helpfile. This will tell the type of the good.
#     name = instCpCodeMgr.CodeToName(code)
#     print(i, code, secondCode, name)
#
# # Obtaining open prices of a stock of last ten days.
#
instStockChart = win32com.client.Dispatch("CpSysDib.StockChart")
#
# instStockChart.SetInputValue(0, "A003540")  # 0 = stock code <- Requesting for a specific stock
# instStockChart.SetInputValue(1, ord("2"))  # 1 = the type of the request, ord('2') = request by the quantity.
# instStockChart.SetInputValue(4, 10)  # 4 = the number of request, 10 = the exact number of the data requested.
# instStockChart.SetInputValue(5, 5)  # 5 = the type of information requesting for, 5 = close price
# instStockChart.SetInputValue(6, ord('D'))  # 6 = the type of the chart, ord('D') = daily
# instStockChart.SetInputValue(9, ord('1'))  # 9 = asking whether the adjusting closing price should be applied, ord('1') = Yes.
#
# # The above lines of code is the list of requests that we want to make.
# # and the line below is to actually make the request to the server.
# instStockChart.BlockRequest()  # After this "request", the server is ready to "reply".
#
# numData = instStockChart.GetHeaderValue(3)  # Counting the number of data that we have received.
#
# for i in range(numData):
#     print(instStockChart.GetDataValue(0, i)) # Printing close prices of the recent 10 days.
#
# # Now, we modify the above code to actually get open price, high price, low price, close price, and trading volume.
#
# instStockChart.SetInputValue(0, "A003540")
# instStockChart.SetInputValue(1, ord("2"))
# instStockChart.SetInputValue(4, 10)
# instStockChart.SetInputValue(5, (0, 2, 3, 4, 5, 8))  # second parameter -> 0 = date, 2 = open price, 3 = high price, 4 = low price, 5 = closed price, 8 = trading volume
# instStockChart.SetInputValue(6, ord('D'))
# instStockChart.SetInputValue(9, ord('1'))
#
# instStockChart.BlockRequest()
#
# numData = instStockChart.GetHeaderValue(3)  # the number of each tuples of data
# numField = instStockChart.GetHeaderValue(1)  # the number of data within a single tuple
#
# for i in range(numData):
#     for j in range(numField):
#         print(instStockChart.GetDataValue(j ,i), end=' ')
#     print("")
#
# We do the same job, but this time by giving the range of date.
instStockChart.SetInputValue(0, "A003540")
instStockChart.SetInputValue(1, ord("1"))
instStockChart.SetInputValue(2, 20210812)  # End of the date
instStockChart.SetInputValue(3, 20210730)  # Start of the date
instStockChart.SetInputValue(5, (0, 2, 3, 4, 5, 8))
instStockChart.SetInputValue(6, ord('D'))
instStockChart.SetInputValue(9, ord('1'))

instStockChart.BlockRequest()

numData = instStockChart.GetHeaderValue(3)
numField = instStockChart.GetHeaderValue(1)

for i in range(numData):
    for j in range(numField):
        print(instStockChart.GetDataValue(j ,i), end=' ')
    print("")
