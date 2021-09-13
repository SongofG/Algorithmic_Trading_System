import sqlite3

con = sqlite3.connect("C:/Users/박해인/PycharmProjects/Python_Trading/SQLite/kospi.db")
cursor = con.cursor()

cursor.execute("SELECT * FROM kakao")  # ALL DATA FROM DATABASE
print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())  # NO DATA AVAILABLE SINCE THERE ARE TWO ROWS

cursor.execute("SELECT * FROM kakao")  # CALL DATA AGAIN
print(cursor.fetchall())

cursor.execute("SELECT * FROM kakao")
kakao = cursor.fetchall()  # LIST OF ALL DATA

print(kakao[0][0])  # FIRST ROW, FIRST COLUMN
print(kakao[0][1])
print(kakao[0][2])
