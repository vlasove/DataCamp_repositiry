import sqlite3


conn = sqlite3.connect("test.db")
cur = conn.cursor()


query_create = "CREATE TABLE IF NOT EXISTS user (id INT, rating REAL, name TEXT)"
cur.execute(query_create)


#query_static = "INSERT INTO user VALUES(3, 43.22, 'Lerek')"
# cur.execute(query_static)
# conn.commit()

query_dynamic = "INSERT INTO user VALUES(?, ?, ?)"
temp = (4, 55.55, "John")
#cur.execute(query_dynamic, temp)
# conn.commit()


query_select = "SELECT * FROM user"
for i in cur.execute(query_select):
    # print(i)
    pass


#query_delete = "DELETE  FROM user WHERE name = 'John'"
# cur.execute(query_delete)


query_update = "UPDATE user SET name = 'Lerek' WHERE name = 'Derek'"
cur.execute(query_update)
conn.commit()

for i in cur.execute(query_select):
    print(i)


conn.close()


# CRUD --- CREATE READ UPDATE DELETE
