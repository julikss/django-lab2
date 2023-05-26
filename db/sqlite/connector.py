import sqlite3

class SqliteDB:
    def __init__(self, path: str):
        self.conn = sqlite3.connect(path)
        self.create_table()
    
    def create_table(self):
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS db2 (
                student_id INTEGER PRIMARY KEY NOT NULL,
                course INTEGER NOT NULL,
                group_name TEXT NOT NULL,
                student TEXT NOT NULL,
                subject TEXT NOT NULL
            )''')
    
    def insert(self, data):
        self.conn.execute('''
            INSERT INTO db2 (
                student_id, 
                course, 
                group_name, 
                student, 
                subject) VALUES (?, ?, ?, ?, ?)''', data)

    def delete_records(self):
        self.conn.execute('DELETE FROM db2')

    def select_all_records(self):
        cur = self.conn.execute('SELECT * FROM db2')
        records = cur.fetchall()
        return records

    def __del__(self):
        self.conn.close() 


sqliteDB = SqliteDB("db2.db")