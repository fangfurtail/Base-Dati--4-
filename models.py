from sqlalchemy import Column, Integer, String, Date,ForeignKey
from database import Base

class Student(Base):
    __tablename__ = "student"
    StudentID = Column( Integer, primary_key=True,index=True)
    FirstName = Column(String(40))
    LastName = Column(String(40))
    DateOfBirth = Column(Date)
    Address = Column(String(100))

class Teacher(Base):
    __tablename__ = 'teacher'

    TeacherID = Column(Integer, primary_key=True, index=True)
    FirstName = Column(String(50))
    LastName = Column(String(50))
    Area = Column(String(100))  # Area of Expertise
    Salary = Column(Integer)

class AdministrativeStaff(Base):
    __tablename__ = 'administrative_staff'

    StaffID = Column(Integer, primary_key=True, index=True)
    FirstName = Column(String(50))
    LastName = Column(String(50))
    Role = Column(String(50))
    Salary = Column(Integer)

class School(Base):
    __tablename__ = 'school'

    SchoolID = Column(Integer, primary_key=True, index=True)
    Name = Column(String(100))
    Address = Column(String(100))
    PhoneNumber = Column(String(15))
    Email = Column(String(100))


class Course(Base):
    __tablename__ = 'course'

    CourseCode = Column(String(10), primary_key=True, index=True)
    Name = Column(String(100))
    Credit = Column(Integer)


class Classroom(Base):
    __tablename__ = 'classroom'

    ClassroomID = Column(Integer, primary_key=True, index=True)
    Floor = Column(Integer)
    Capacity = Column(Integer)

class Enrollment(Base):
    __tablename__= 'enrolment'
    StudentID = Column(Integer,ForeignKey())