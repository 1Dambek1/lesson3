

# model
# id
# name
# age


# select(User).where(User.id == 1)
name = {"id": 1, "name": "John", "age": 30}

# """SELECT * FROM users WHERE id = 1;"""
name = [1, "jhon", 15] 



import random
from fastapi import Depends
from fastapi import Depends

from fastapi import Depends

from fastapi import Depends

from fastapi import Depends

from fastapi import Depends


from fastapi import Depends
from fastapi import Depends


from fastapi import Depends

from fastapi import Depends

from fastapi import Depends

from fastapi import Depends

from fastapi import Depends

from fastapi import Depends

from fastapi import Depends

from fastapi import Depends

from fastapi import Depends

from sqlalchemy import create_engine,text
from sqlalchemy.orm import sessionmaker, Session

engine = create_engine(url = 'sqlite:///mydatabase.db')
connection = sessionmaker(bind = engine)


# with connection() as session:

    


from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

class Base(DeclarativeBase):
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)



class User(Base):
    __tablename__ = 'user'
    
    # id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    # name = Column(String(50))
    # age = Column(Integer)
    
    name:Mapped[str]
    age:Mapped[int]
    

class Product(Base):
    __tablename__ = 'product'
    
    name:Mapped[str]
    price:Mapped[float] 
    desc:Mapped[str]
    
    
Base.metadata.create_all(engine)

def create_users():
        session = connection()
        
        for i in range(100000):
            user = User(name=f'{i}J{i*"k"}ohn', age=2*10)
            session.add(user)
        session.commit()

from sqlalchemy import select

import time
from sqlalchemy import func
def get_all_users_scalars():
        time_start = time.time()
    
        session = connection()
        data = session.scalars(select(User))
        data = data.all()
        times = (time.time() - time_start)
        print(times)
        return times
def get_all_users_execute():
    time_start = time.time()
    session = connection()
    
    data = session.execute(select(User))
    data = data.all()
    times = (time.time() - time_start)
    print(times)
    return times

# def get_11_object():
#     session = connection()
#     user =session.get(User, 11)
#     return user.__dict__    
# def delete_users():
#     session = connection()
#     data = session.scalar(select(User).where(User.id == 10))
    
#     session.delete(data)
#     session.commit()
#     return True

# def update_11_user(age:int = int(input())):
#     session = connection()
#     user =session.get(User, 11)
#     user.age = age
    
#     session.commit()
#     return True
    
    
# # # data = session.scalar(select(User).where(User.id > 1))
# # data = session.scalars(select(User).where(User.id > 1))
# # data = session.execute(select(User.id, func.sum(User.age)).where(User.id > 1))
# create_users()

# s_time = get_all_users_scalars()
# print("_"*100)
# e_time = get_all_users_execute()

# print(e_time-s_time)

# delete_users()
# update_11_user()
# print(get_11_object())

# session = session()
# session.commit()

# 2
# with connection() as session:
#     ...
#     session.commit()

# # 3
# def get_session():
#     with connection() as session:
#         yield session
#         session.commit()
        

        


#  postgresql://postgres@localhost/mydatabase**
# import psycopg2
# connection = psycopg2.connect(
#     host="localhost",
#     database="mydatabase",
#     user="postgres",
#     password="postgres"
# )



# from sqlalchemy.orm import Mapped, mapped_column
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import DeclarativeBase
# from sqlalchemy import Column, Integer, String

# # Base = declarative_base()

# class Base(DeclarativeBase):
#     id:Mapped[int] = mapped_column(primary_key = True)


# class User(Base):
#     __tablename__ = "users"
    
#     name:Mapped[str] = mapped_column(unique=True)
#     age:Mapped[int]


    

# # print(Base.metadata.tables)
# # Base.metadata.create_all(engine)
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.orm import Session

# Sessiona = sessionmaker(bind=engine)

# # 
# # session:Session = Sessiona()?
# def get_session():
#     with Sessiona() as session:
#         yield session
#         session.commit()
        
# # for i in range(100): 
# #     user = User(name = f"{random.randint(10, 80)}Jo{random.randint(10, 80)}hn{i}", age = random.randint(10, 80))
# #     session.add(user)
# # session.commit()

# # data = session.scalar
# # data = session.scalars
# # data = session.execute


# """SELECT * FROM users WHERE id = 1;"""
# # data = session.query(User).where(User.id == 1).all()
# # print(data[0].name)
# from sqlalchemy import select,text

# # [1,2,3,4]


# # data = session.scalar
# # print(select(User.id, User.name).where(User.id == 25).order_by(User.name).limit(20))
# from pydantic import BaseModel

# class UserSchema(BaseModel):
#     id:int
#     name: str
#     age: int

# from fastapi import FastAPI, Depends
# app = FastAPI()

# @app.get("/users/{id}", response_model=list[UserSchema])
# def read_user(sessison:Session = Depends(get_session)):
#     # data = session.query(User).where(User.id == id).all()
#     data = sessison.scalars(select(User))
#     return data.all()

# # one_or_none()
# # one()
# # all()
# fetchall()
# fetchone()

# print("commands")
# # 1 list users
# # 2 add user
# # 3 get user by id
# # 4 order users by age
# # Сделать Приожение в терминале, где в цикле будет выполняться определенные команды, в зависимости от цифры, которую введет пользователь
# # Обязательно должны быть типизация(pydantic) и все функции должны быть с примерами
# while True:
    
#     command = input("Enter command: ")
#     if command == "1":
#         create_user(input("Enter name: "), input("Enter age: ")) # function
#     elif command == "2":
#         ...
        