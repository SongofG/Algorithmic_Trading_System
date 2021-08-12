import win32com.client

# 1. Checking the connection to the CYBOS Plus API
instCpCybos = win32com.client.Dispatch("CpUtil.CpCybos")
print(instCpCybos.IsConnect)  # This prints 1 if the API is connected to the server. Otherwise, prints 0.
#
# # 2. Counting the number of companies went up to Korean stock market.
# instCpStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")
# print(instCpStockCode.GetCount())  # The code below will print 3410 (12/08/2021)
#
# # 3. Getting specific stock information.
# # The first parameter inside ".GetData()" is given to specify the type of data we get
# # The second parameter is the index of specific stock item
# print(instCpStockCode.GetData(1, 0))  # "1" for the first parameter returns the name of the given index's stock
# print(instCpStockCode.GetData(0, 0))  # "0" for the first parameter returns the code of the given index's stock
#
# # Using for loop to obtain the first 10 stocks in the list
# for i in range(0,10):
#     print(instCpStockCode.GetData(1, i))
#
# # 4. Using for loop to find a stock of "Naver"
# instCpStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")
# stockNum = instCpStockCode.GetCount()
#
# for i in range(stockNum):
#     if instCpStockCode.GetData(1, i) == 'NAVER':
#         print(instCpStockCode.GetData(0,i))
#         print(instCpStockCode.GetData(1,i))
#         print(i)
#
# # 5. Using built-in methods to find a stock of "Naver"
# instCpStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")
#
# naverCode = instCpStockCode.NameToCode('NAVER')  # name of the stock as input, and the code for the output.
# naverIndex = instCpStockCode.CodeToIndex(naverCode)
# print(naverCode)
# print(naverIndex)
