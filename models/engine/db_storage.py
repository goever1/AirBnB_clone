#!/usr/bin/python3
"""
Defines a new engine of storage
Database mode, to be used with SQLAlchemy
"""
from os import getenv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import Session, sessionmaker, scoped_session
import models
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.base_model import BaseModel, Base

class DBStorage:
  """
  Create our database with SQLAlchemy
  """
  __enginde = None
  __session = None

  def __init__(self):
    user = getenv('HBNB_MYSQL_USER')
    pwd = getenv('HBNB_MYSQL_PWD')
    host = getenv('HBNB_MYSQL_HOST')
    database = getenv('HBNB_MYSQL_DB')
    self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                  .format(user, pwd, host, database),
                                  pool_pre_ping=True)
    if getenv('HBNB_ENV') == 'test':
      Base.metadata.drop_all(self.__engine)

def all(self, cls=None):
  obj_dict = {}
  if cls != '':
    objs = self.__session.query(cls)
  else:
    objs = self.__session.query(Amenity)
    objs += self.__session.query(City)
    objs += self.__session.query(Place)
    objs += self.__session.query(Review)
    objs += self.__session.query(State)
    objs += self.__session.query(User)
  return {"{}.{}".format(obj.__class__.__name__, obj.id): obj
          for obj in objs}

  def new(self, obj):
      self.__session.add(obj)

  def save(self):
      self.__session.commit()
  
  def delete(self, obj):
      if obj:
        self.__session.delete(obj)

  def reload(self):
      Base.metadata.create_all(self.__engine)
      session_factory = sessionmaker(
          bind=self.__engine, expire_on_commit=False)
      Session = scoped_session(session_factory)
      self.__session = Session

  def close(self):
       self.__session.remove()
    
  def classes(self):
        """ returns dictionary of valid classes """
