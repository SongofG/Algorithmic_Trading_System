import win32com.client
instCpStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")

# The code below will print 3410 (12/08/2021, Wednesday)
# 3409 means that there are 3410 companies that went public to the Korean market.
print(instCpStockCode.GetCount())


