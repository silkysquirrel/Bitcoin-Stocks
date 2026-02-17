
import pandas as pd
import sqlite3


conn = sqlite3.connect('data/mydatabase.db')
cursor = conn.cursor()

# cursor.execute("SELECT * FROM bitcoin_data")
# rows = cursor.fetchall()
# for row in rows:
#     print(row)


# Retrieve data from database to do analysis and manipulation
df = pd.read_sql_query("SELECT * FROM bitcoin_data", conn)

print(df)


conn.close()
