# Since the trading volume of a market is hardly framed up,
# it is a good figure to capture a pattern.
# We can develop an algorithm to find a prospective stock by using the figure
# There are two criteria
# 1. Mass trading volume should be captured (1,000% increase in the trading volume) <- Use the StockChart Class
# 2. During the mass trading, the PBR should be less than 4

import win32com.client

# Create object
instStockChart = win32com.client.Dispatch("CpSysDib.StockChart")
instCpStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")  # For printing the name of the stock

# SetInputValue
instStockChart.SetInputValue(0, instCpStockCode.NameToCode('대신증권'))
instStockChart.SetInputValue(1, ord('2'))
instStockChart.SetInputValue(4, 60)
instStockChart.SetInputValue(5, 8)  # Remember that 8 for the second parameter is the trading volume
instStockChart.SetInputValue(6, ord('D'))
instStockChart.SetInputValue(9, ord('1'))

# BlockRequest
instStockChart.BlockRequest()

# GetData
volumes = []
numData = instStockChart.getHeaderValue(3)
for i in range(numData):
    volume = instStockChart.GetDataValue(0, i)
    volumes.append(volume)

print(instCpStockCode.CodeToName(instCpStockCode.NameToCode('대신증권')))
print(volumes)

# Average of all volumes except the first day.
averageVolume = (sum(volumes) - volumes[0])/(len(volumes) - 1)
if volumes[0] > averageVolume * 10:
    print('대박 주')
else:
    print('일반 주', volumes[0]/averageVolume)
