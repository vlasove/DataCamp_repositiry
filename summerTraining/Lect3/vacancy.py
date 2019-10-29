import sqlite3


class Vacancy:
    def __init__(self, title, employer, salary):
        self.Title = title
        self.Employer = employer
        self.Salary = salary

    def insert(self):
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()

        query_check = "CREATE TABLE IF NOT EXISTS vac (title TEXT, employer TEXT, salary REAL)"
        cur.execute(query_check)

        query_insert = "INSERT INTO vac VALUES(?, ?, ?)"
        data = (self.Title, self.Employer, self.Salary)
        cur.execute(query_insert, data)
        conn.commit()

        conn.close()
