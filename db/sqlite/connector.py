import peewee as pw

class SqliteDB:
    def __init__(self):
        self.db = pw.SqliteDatabase('db2.db')
        self.db.connect()
        self.create_table()
    
    def create_table(self):
        class DecanatModel(pw.Model):
            student_id = pw.IntegerField(primary_key=True)
            course = pw.IntegerField(null=False)
            group_name = pw.CharField(null=False)
            student = pw.CharField(null=False)
            subject = pw.CharField(null=False)

            class Meta:
                database = self.db
                table_name = 'db2'

        self.decanat = DecanatModel
        self.db.create_tables([DecanatModel])
    
    def insert(self, data):
        self.decanat.create(student_id=data[0], course=data[1], group_name=data[2], student=data[3], subject=data[4])

    def delete_records(self):
        q = self.decanat.delete()
        q.execute()

    def select_all_records(self):
        data = list(self.decanat.select().tuples())
        return data

    def __del__(self):
        self.db.close() 


sqliteDB = SqliteDB()