# This python file is to check the connection of the Daisin API.
import win32com.client  # This is a type of COM(Component Object Model).
instCpCybos = win32com.client.Dispatch("CpUtil.CpCybos")
print(instCpCybos.IsConnect)  # This prints 1 if the API is connected to the server. Otherwise, prints 0.
