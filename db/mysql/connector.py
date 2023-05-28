import peewee as pw

class MysqlDB():
    def __init__(self):
        self.db = pw.MySQLDatabase(
            'decanatdb',
            user = 'root',
            password = 'Passwd1!',
            host = 'localhost'
        )

        self.create_table()

    def create_table(self):
        class DecanatModel(pw.Model):
            student_id = pw.IntegerField(primary_key=True)
            course = pw.IntegerField(null=False)
            group_name = pw.CharField(null=False)
            student = pw.CharField(null=False)
        
            class Meta:
                database = self.db
                table_name = 'db3'

        self.decanat = DecanatModel
        self.db.create_tables([DecanatModel], safe=True)
         
    def select_all_records(self):
        rows = list(self.decanat.select().dicts())
        return [(row['student_id'], row['course'], row['group_name'], row['student']) for row in rows]

    def insert(self, record):
        self.decanat.create(
            student_id=record[0], course=record[1], group_name=record[2], student=record[3]
        )
    
    def delete_records(self):
        self.decanat.delete().execute()

mysqlDB = MysqlDB()