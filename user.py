from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

DeclarativeBase = declarative_base()


class User(DeclarativeBase):
    __tablename__ = 'users2'

    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column('login', String)
    password = Column('password', String)
    name = Column('name', String)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

# class User3(DeclarativeBase):
#     __tablename__ = 'users3'
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     login = Column('login', String)
#     password = Column('password', String)
#     name = Column('name', String)
#
#     def __repr__(self):
#         return "".format(self.code)
