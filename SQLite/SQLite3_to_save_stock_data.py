import pandas as pd
import pandas_datareader.data as web
import datetime
import sqlite3

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2016, 6, 12)
df = web.DataReader("078930.KS", "yahoo", start, end)  # 078930 IS STOCK CODE FOR GS
# print(df.head())

con = sqlite3.connect("C:/Users/박해인/PycharmProjects/Python_Trading/SQLite/kospi.db")
df.to_sql('078930', con, if_exists='replace')  # if_replace: DELETE THE PREVIOUS TABLE AND INSERT NEW TABLE

read_df = pd.read_sql("SELECT * FROM '078930'", con, index_col='Date')  # CHECK THE UPDATED TABLE DATA
# print(read_df.head())
