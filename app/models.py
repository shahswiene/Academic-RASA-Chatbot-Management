from datetime import datetime
from app import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    student_id = db.Column(db.String(120), unique=True, nullable=False)
    faculty = db.Column(db.String(120), nullable=False)
    course = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    registered_on = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Student {}>'.format(self.email)
