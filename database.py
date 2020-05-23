import sqlite3


class Db:
    def __init__(self, db):
        self.db = sqlite3.connect(db)
        self.cursor = self.db.cursor()
        command = "CREATE TABLE IF NOT EXISTS members (id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, " \
                  "email TEXT, " \
                  "phone INTEGER, home_address TEXT) "
        self.cursor.execute(command)
        self.db.commit()

    def fetch(self, first_name, email):
        command = 'SELECT * FROM members WHERE first_name=? AND email=?'
        value = (first_name, email)
        self.cursor.execute(command, value)
        rows = self.cursor.fetchall()
        return rows

    def insert(self, first_name, last_name, email, phone, home_address):
        command = 'INSERT INTO members VALUES (NULL, ?, ?, ?, ?,?)'
        value = (first_name, last_name, email, phone, home_address)
        self.cursor.execute(command, value)
        self.db.commit()

    def __del__(self):
        self.cursor.close()
