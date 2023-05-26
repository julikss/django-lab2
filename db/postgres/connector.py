import psycopg2

class PostgresDB:
    def __init__(self, path: str):
        self.conn = psycopg2.connect(path)
        self.create_table()
        self.fill_with_test_values()
    
    def create_table(self):
        cur = self.conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS db1 (
                student_id INTEGER PRIMARY KEY NOT NULL,
                course INTEGER NOT NULL,
                group_name TEXT NOT NULL,
                student TEXT NOT NULL,
                subject TEXT NOT NULL
            )''')
        cur.close()

    def fill_with_test_values(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM db1")
        records = cur.fetchall()
        empty = len(records)
        if empty == 0:            
            script = open('db/postgres/example.sql', 'r').read()
            cur.execute(script)
            cur.close()

    def read(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM db1")
        records = cur.fetchall()
        return records
    
    def create(self, data):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO db1 (student_id, course, group_name, student, subject) VALUES (%s, %s, %s, %s, %s)", data)
        cur.close()

    def update(self, data):
        cur = self.conn.cursor()
        cur.execute("UPDATE db1 SET course = %s, group_name = %s, student = %s, subject = %s WHERE student_id = %s", 
                    (data[1], data[2], data[3], data[4], data[0]))
        cur.close()
    
    def delete(self, id):
        cur = self.conn.cursor()
        cur.execute("DELETE FROM db1 WHERE student_id = %s", [id])
        cur.close()
    
    def get_student(self, id):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM db1 WHERE student_id = %s", [id])
        student = cur.fetchall()
        cur.close()
        return student


postgresDB = PostgresDB("dbname=decanatdb user=postgres password=password")