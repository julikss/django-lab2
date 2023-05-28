import peewee as pw
from db.postgres.example import example_students
class PostgresDB:
    def __init__(self):
        self.db = pw.PostgresqlDatabase(
            'decanatdb',
            user = 'postgres',
            password='password'
        )
        self.create_table()
        self.fill_with_test_values()
    
    def create_table(self):
        class DecanatModel(pw.Model):
            student_id = pw.IntegerField(primary_key=True)
            course = pw.IntegerField(null=False)
            group_name = pw.CharField(null=False)
            student = pw.CharField(null=False)
            subject = pw.CharField(null=False)

            class Meta:
                database = self.db
                table_name = 'db1'

        self.decanat = DecanatModel
        self.db.create_tables([DecanatModel], safe=True)

    def fill_with_test_values(self):
        records = self.decanat.select()
        empty = len(records)
        if empty == 0:            
            q = self.decanat.insert_many(example_students)
            q.execute()

    def read(self):
        data = self.decanat.select().tuples()
        return data
    
    def create(self, data):
        self.decanat.create(student_id=data[0], course=data[1], group_name=data[2], student=data[3], subject=data[4])

    def update(self, data):
        student = self.decanat.get(self.decanat.student_id == data[0])
        student.course = data[1]
        student.group_name = data[2]
        student.student = data[3]
        student.subject = data[4]
        student.save()
    
    def delete(self, id):
        student = self.decanat.get(self.decanat.student_id == id)
        student.delete_instance()
    
    def get_student(self, id):
        student = self.decanat.get(self.decanat.student_id == id)
        return student

postgresDB = PostgresDB()