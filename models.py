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

    CourseCode = Column(Integer, primary_key=True, index=True)
    Name = Column(String(100))
    Credit = Column(Integer)


class Classroom(Base):
    __tablename__ = 'classroom'

    ClassroomID = Column(Integer, primary_key=True, index=True)
    Floor = Column(Integer)
    Capacity = Column(Integer)

class Enrollment(Base):
    __tablename__= 'enrollment'

    EnrollmentDate = Column(Date)
    StudentID = Column(Integer,ForeignKey('student.StudentID'),primary_key=True)
    CourseCode= Column(Integer,ForeignKey('course.CourseCode'),primary_key=True )
    

class Teaches(Base):
    __tablename__ ='teaches'

    TeacherID = Column(Integer,ForeignKey('teacher.TeacherID'),primary_key=True)
    CourseCode= Column(Integer,ForeignKey('course.CourseCode'),primary_key=True )

class HeldIn(Base):
    __tablename__ = 'heldin'

    CourseCode= Column(Integer,ForeignKey('course.CourseCode'),primary_key=True )
    ClassroomID = Column(Integer , ForeignKey('classroom.ClassroomID'),primary_key=True)

class WorksFor(Base):
    __tablename__ = 'works_for'

    StaffID = Column(Integer, ForeignKey('administrative_staff.StaffID'), primary_key=True)
    SchoolID = Column(Integer, ForeignKey('school.SchoolID'), primary_key=True)
