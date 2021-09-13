import pandas as pd
import sqlite3

con = sqlite3.connect("C:/Users/박해인/PycharmProjects/Python_Trading/SQLite/kospi.db")
df = pd.read_sql("SELECT * FROM kakao", con, index_col=None)  # SQL TO DATAFRAME
print(df)

df = pd.read_sql("SELECT * FROM test", con, index_col="index")  # THE FIRST COLUMN IS INDEX
print(df)
