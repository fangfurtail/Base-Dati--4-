from models import Student
from datetime import date
from database import SessionLocal , engine, Base

Base.metadata.create_all(bind=engine)
session = SessionLocal()

def list_students():
    students = session.query(Student).all()
    for student in students:
        print(f"{student.StudentID}: {student.FirstName} {student.LastName}, DOB: {student.DateOfBirth}, Address: {student.Address}")

list_students()