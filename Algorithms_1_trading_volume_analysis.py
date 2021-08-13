# Building a function
import win32com.client
import time


def CheckVolume(instStockChart, code):  # this method takes in the StockChart instance and the code as its parameter.
    # SetInputValue
    instStockChart.SetInputValue(0, code)
    instStockChart.SetInputValue(1, ord('2'))
    instStockChart.SetInputValue(4, 60)
    instStockChart.SetInputValue(5, 8)
    instStockChart.SetInputValue(6, ord('D'))
    instStockChart.SetInputValue(9, ord('1'))

    # BlockRequest
    instStockChart.BlockRequest()

    # GetDate
    volumes = []
    numData = instStockChart.GetHeaderValue(3)
    for i in range(numData):
        volume = instStockChart.GetDataValue(0, i)
        volumes.append(volume)

    # Calculate average volume
    averageVolume = (sum(volumes) - volumes[0]) / (len(volumes) - 1)

    if volumes[0] > averageVolume * 10:
        return 1
    else:
        return 0


if __name__ == "__main__":  # Run the code below only when it's ran by itself, not imported to other files.
    instStockChart = win32com.client.Dispatch("CpSysDib.StockChart")
    instCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
    instCpStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")
    codeList = instCpCodeMgr.GetStockListByMarket(1)
    buyList = []
    start = time.time()
    for code in codeList:
        if CheckVolume(instStockChart, code) == 1:
            buyList.append(code)
            print(instCpStockCode.CodeToName(code))
        time.sleep(0.75)
    print('시간:', start - time.time())
