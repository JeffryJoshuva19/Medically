from sqlalchemy import Boolean, Column, ForeignKey,  String, DateTime, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Time,Date,DateTime,BLOB, JSON,Float
from sqlalchemy.orm import relationship
from datetime import date, datetime
from database import engine
#import bcrypt
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
Base.metadata.bind = engine

class User(Base):
    __tablename__ = 'users'
    
    id=Column(Integer,index=True,autoincrement=True, primary_key=True,nullable=False)
    Name=Column(String(255),nullable=False)
    Occupation=Column(String(255),nullable=False)
    Dob=Column(String(255),nullable=False)
    Location=Column(String(255),nullable=False)
    City=Column(String(255),nullable=False)
    Username=Column(String(255),nullable=False)
    Emailid=Column(String(255),nullable=False)
    Password=Column(String(255),nullable=False)
    Cover_IMG=Column(String(255),nullable=False)
    Thumb_IMG=Column(String(255),nullable=False)
    #command  columns
    Position=Column(String(255),nullable=True)
    Website=Column(String(255),nullable=True)
    Status=Column(String(100),nullable=False)
    Aboutus=Column(String(500),nullable=False)
    Interest=Column(String(400),nullable=False)
    Certificates=Column(String(255),nullable=True)
    verify=Column(String(255),nullable=True)
    Created_at=Column(String(100),nullable=False)

class Posts(Base):
    __tablename__ = 'posts'
    
    id=Column(Integer,index=True,autoincrement=True, primary_key=True,nullable=False)
    Postid=Column(String(255),nullable=False)
    Username=Column(String(255),nullable=False)
    Postimage=Column(String(255),nullable=False)
    Posttitle=Column(String(255),nullable=False)
    Postdescription=Column(String(255),nullable=False)
    Likes=Column(String(255),nullable=False)
    comments=Column(String(255),nullable=False)
    #command columns
    Status=Column(String(100),nullable=False)
    Created_at=Column(String(100),nullable=False)

class Advertisement(Base):
    __tablename__ = 'advertisement'
    id=Column(Integer,index=True,autoincrement=True, primary_key=True,nullable=False)
    image=Column(String(255),nullable=False)
    Status=Column(String(100),nullable=False)
    Created_at=Column(String(100),nullable=False)

class Comments(Base):
    __tablename__ = 'comments'
    id=Column(Integer,index=True,autoincrement=True, primary_key=True,nullable=False)
    Postid=Column(String(255),nullable=False)
    Comments=Column(String(100),nullable=False)
    Username=Column(String(100),nullable=False)
    Created_at=Column(String(100),nullable=False)

class Menus(Base):
    __tablename__ = 'menus'
    id=Column(Integer,index=True,autoincrement=True, primary_key=True,nullable=False)
    Menuname=Column(String(255),nullable=False)
    Status=Column(String(100),nullable=False)
    Created_at=Column(String(100),nullable=False)

class Infectious(Base):
    __tablename__ = 'infectious'
    id=Column(Integer,index=True,autoincrement=True,primary_key=True,nullable=False)
    image=Column(String(255),nullable=False)
    text=Column(String(255),nullable=False)
    price=Column(String(255),nullable=False)
    Status=Column(String(100),nullable=False)
    Created_at=Column(String(100),nullable=False)

class Research(Base):
    __tablename__ = 'research'
    id=Column(Integer,index=True,autoincrement=True,primary_key=True,nullable=False)
    text=Column(String(255),nullable=False)
    link=Column(String(255),nullable=False)
    Status=Column(String(100),nullable=False)
    Created_at=Column(String(100),nullable=False)

class Circle(Base):
    __tablename__ = "circle"
    
    id = Column(Integer, primary_key=True,index=True)
    image=Column(String(255))
    name=Column(String(255))
    circle_status=Column(String(255))
    Created_at=Column(String(100),nullable=False)

Base.metadata.create_all(bind=engine)