# In Korean stock market, each of the stocks carry unique code.

import win32com.client

instCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")  # CpCodeMgr class is for getting variety of code info.
codeList = instCpCodeMgr.GetStockListByMarket(1)  # This returns a tuple of Korean stock market's items
print(codeList)

# 1. Make a dictionary which has the stock codes as "keys" and the stock names as "values"
kospi = {}
for code in codeList:
    name = instCpCodeMgr.CodeToName(code)
    kospi[code] = name

# 2. Export the kospi dictionary into a csv file format.
f = open("C:/Users/박해인/PycharmProjects/Python_Trading/kospi.csv", 'w')  # the second parameter is to "write" a file
for key, value in kospi.items():
    f.write("%s, %s\n" % (key, value))
f.close()
