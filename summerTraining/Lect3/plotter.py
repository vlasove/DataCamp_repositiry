import matplotlib.pyplot as plt
import sqlite3


conn = sqlite3.connect("data.db")
cur = conn.cursor()

query = "SELECT salary FROM vac"
salary_list = []
for item in cur.execute(query):
    salary_list.append(item[0])


plt.title("Salary Distribute")
plt.xlabel("Salary Value")
plt.ylabel("Count")
plt.hist(salary_list, bins=40, alpha=0.7)
plt.grid(True)
plt.show()

conn.close()
