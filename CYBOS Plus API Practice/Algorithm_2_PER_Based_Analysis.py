# This time, we are using PER to analyse stock values.
# As an example, we are going to analyse Grocery industry.

import win32com.client

instCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
instMarketEye = win32com.client.Dispatch("CpSysDib.MarketEye")

# industryCodeList = instCpCodeMgr.GetIndustryList()  # Returns code list of industries.
# for industryCode in industryCodeList:
#     print(industryCode, instCpCodeMgr.GetIndustryName(industryCode))  # Prints the list of codes and industries

targetCodeList = instCpCodeMgr.GetGroupCodeList(5)  # 5 is the code for the grocery industry.
# for code in targetCodeList:
#     print(code, instCpCodeMgr.CodeToName(code))  # Prints the list of codes and the names of companies

# Get PER
instMarketEye.SetInputValue(0, 67)  # 67 <= PER from http://cybosplus.github.io/
instMarketEye.SetInputValue(1, targetCodeList)  # Input <= stock codes of the industry

# BlockRequest
instMarketEye.BlockRequest()

# GetHeaderValue
numStock = instMarketEye.GetHeaderValue(2)

# GetData
sumPer = 0
for i in range(numStock):
    sumPer += instMarketEye.GetDataValue(0, i)

print(instMarketEye.GetHeaderValue(0))  # Prints the num of requests
print(instMarketEye.GetHeaderValue(1))  # Prints a tuple of the names of the requests
print(instMarketEye.GetHeaderValue(2))  # Prints the num of stocks
print("Average PER:", sumPer/numStock)
