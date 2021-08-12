# PER(Price Earning Ratio, 주가 이익 비율): If a company's stock price is $5 and its profit is $1
# than the PER is 5. Higher the PER, more the stock price is overrated compared to the profit earned.
# Lower the PER, less the stock price is underrated compared to the profit earned.

import win32com.client

# Create Object
instMarketEye = win32com.client.Dispatch("CpSysDib.MarketEye")
instCpStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")  # For getting the name of the stock.

# SetInputValue
instMarketEye.SetInputValue(0, (4, 67, 70, 111))
instMarketEye.SetInputValue(1, 'A003540')

# BlockRequest
instMarketEye.BlockRequest()

# GetData
print('종목 이름:', instCpStockCode.CodeToName('A003540'))
print('현재가:', instMarketEye.getDataValue(0, 0))  # the first parameter is the index inside specific stock item
print('PER:', instMarketEye.GetDataValue(1, 0))  # the second parameter is the index of stock items
print('EPS:', instMarketEye.GetDataValue(2, 0))
print('최근분기년월:', instMarketEye.GetDataValue(3, 0))
