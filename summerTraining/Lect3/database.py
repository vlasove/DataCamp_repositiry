import sqlite3

conn = sqlite3.connect("data.db")
cur = conn.cursor()


query_select = "SELECT * FROM vac"

for item in cur.execute(query_select):
    print(item)
