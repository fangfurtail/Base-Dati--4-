from sqlalchemy import Column, Integer, String, Date
from database import Base

class Student(Base):
    __tablename__ = "Student"
    StudentID = Column( Integer, primary_key=True,index=True)
    FirstName = Column(String(40))
    