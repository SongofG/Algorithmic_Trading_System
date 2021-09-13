# IMPORT SQLITE
import sqlite3
# print(sqlite3.version) # VERSION CHECK
# print(sqlite3.sqlite_version)

con = sqlite3.connect("C:/Users/박해인/PycharmProjects/Python_Trading/SQLite/kospi.db") # CREATE DATABASE
# print(type(con)) # CHECK TYPE
cursor = con.cursor()

# CREATE TABLE "KAKAO"
cursor.execute("CREATE TABLE kakao(Date text, Open int, High int, Low int, Closing int, Volume int)")
cursor.execute("INSERT INTO kakao VALUES('16.06.03', 97000, 98600, 96900, 98000, 321405)") # INSERT DATA
cursor.execute("INSERT INTO kakao VALUES('16.06.02', 99000, 99300, 96300, 97500, 556790)") # INSERT DATA

con.commit() # APPLY TO THE DATABASE
con.close() # CLOSE THE DATABASE
