#!/usr/bin/python3
"""
Defines a new engine of storage
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.user import User
from models.review import Review
from models.amenity import Amenity


class DBStorage:
  
  __engine = None
  __session = None

  def __init__(self):
    user = os.environ.get('HBNB_MYSQL_USER')
    pwd = os.environ.get('HBNB_MYSQL_PWD')
    host = os.environ.get('HBNB_MYSQL_HOST')
    db = os.environ.get('HBNB_MYSQL_DB')
    self.engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                .format(user, pwd, host, db), 
                                pool_pre_ping=True)
    if os.environ.get('HBNB_ENV') == 'test':
      Base.metadata.drop_all(bind=self.__engine)

  def all(self, cls=None):
    objs = {}
    if cls == None:
      classes = [BaseModel, State, City, place, Review]
    else:
      classes = [cls]

    for c in classes:
      for obj in self.__session.query(c).all():
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        objs[key] = obj
    return objs

  def new(self, obj):
    self.__session.add(obj)

  def save(self):
    self.__session.commit()

  def delete(self, obj=None):
    if obj != None:
      self.__session,delete(obj)

  def reload(self):
    Base.metadata.create_all(bind=self.__engine)
    self.__session = scoped_session(sessionmaker(bind=self.__engine, 
                                                 expire_on_commit=False))

  def close(self):
        """close session, proper ending"""
        self.__session.remove()

  def classes(self):
        """ returns dictionary of valid classes """
