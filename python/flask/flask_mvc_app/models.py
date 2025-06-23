from config import db,app


class Employee(db.Model):
    id = db.Column('emp_id',db.Integer(),primary_key=True)
    name = db.Column('emp_name',db.String(50))
    salary = db.Column('emp_salary',db.Float())
    role = db.Column('emp_role',db.String(40))


with app.app_context():
    db.create_all()