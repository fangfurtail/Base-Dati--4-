from models import Student
from datetime import date
from database import SessionLocal , engine, Base

session = SessionLocal()

def list_students():
    students = session.query(Student).all()
    for student in students:
        print(f"{student.StudentID}: {student.FirstName} {student.LastName}, DOB: {student.DateOfBirth}, Address: {student.Address}")

def add_student():
    sid = int(input("Student ID: "))
    fname = input("First Name: ")
    lname = input("Last Name: ")
    dob = input("Date of Birth (YYYY-MM-DD): ")
    address = input("Address: ")

    new_student = Student(
    StudentID=sid,
    FirstName=fname,
    LastName=lname,
    DateOfBirth=date.fromisoformat(dob),
    Address=address
    )
    session.add(new_student)
    session.commit()
    print("Student added successfully!")


def delete_student():
    sid = int(input("Enter Student ID to delete: "))
    student= session.query(Student).where(Student.StudentID == sid).first()

    if student:
        session.delete(student)
        session.commit()
        print("Student deleted successfully!")
    else:
        print("Student not found.")

def update_student():
    sid = int(input("Enter Student ID to update: ")) 
    student = session.query(Student).filter(Student.StudentID == sid).first()  

    if student:
       
        print(f"Current Info - Name: {student.FirstName} {student.LastName}, DOB: {student.DateOfBirth}, Address: {student.Address}")

        fname = input("New First Name (leave blank to keep current): ")
        lname = input("New Last Name (leave blank to keep current): ")
        dob = input("New Date of Birth (YYYY-MM-DD) (leave blank to keep current): ")
        address = input("New Address (leave blank to keep current): ")

        if fname:
            student.FirstName = fname
        if lname:
            student.LastName = lname
        if dob:
            try:
                student.DateOfBirth = date.fromisoformat(dob)
            except ValueError:
                print("Invalid date format! Date not updated.")
        if address:
            student.Address = address

        session.commit()  
        print("Student updated successfully!")
    else:
        print("Student not found.")  


def main():
    while True:
        print("\n1. Add Student\n2. List Students\n3. Delete Student\n4. Update Student\n5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            list_students()
        elif choice == '3':
            delete_student()
        elif choice == '4':
            update_student()  
        elif choice == '5':
            break
        else:
            print("Invalid choice!")


main()