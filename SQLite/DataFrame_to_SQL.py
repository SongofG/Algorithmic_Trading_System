import pandas as pd
import sqlite3

raw_data = {'col0':[1, 2, 3, 4], "col1":[10, 20, 30, 40], "col2":[100, 200, 300, 400]}
df = pd.DataFrame(raw_data)
con = sqlite3.connect("C:/Users/박해인/PycharmProjects/Python_Trading/SQLite/kospi.db")

df.to_sql('test', con)  # DATAFRAME TO SQL. TABLE NAME: test, CURSOR OBJECT: con
