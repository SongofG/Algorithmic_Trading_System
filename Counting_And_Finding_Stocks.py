import win32com.client

# 1. Checking the connection to the stock market server.
instCpCybos = win32com.client.Dispatch("CpUtil.CpCybos")
print(instCpCybos.IsConnect)  # This prints 1 if the API is connected to the server. Otherwise, prints 0.

# 2. Counting the number of companies went up to Korean stock market.
instCpStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")
print(instCpStockCode.GetCount())  # The code below will print 3410 (12/08/2021)

# 3. Getting specific stock information.
# The first parameter inside ".GetData()" is given to specify the type of data we get
# The second parameter is the index of specific stock item
print(instCpStockCode.GetData(1, 0))
