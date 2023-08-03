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
from models.place import Place

class DBStorage:
  
  __engine = None
  __session = None

  def __init__(self):
    user = os.environ.get('HBNB_MYSQL_USER')
    pwd = os.environ.get('HBNB_MYSQL_PWD')
    host = os.environ.get('HBNB_MYSQL_HOST')
    db = os.environ.get('HBNB_MYSQL_DB')
    self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                .format(user, pwd, host, db), 
                                pool_pre_ping=True)
    if os.environ.get('HBNB_ENV') == 'test':
      Base.metadata.drop_all(bind=self.__engine)

  def all(self, cls=None):
      """
      Perform query on the current database session
      # Must return a dictionary with all objects according
      to class name passed in cls argument
      """
      obj_dict = {}
      if cls != '':
          objs = self.__session.query(cls)
      else:
          objs = self.__session.query(Amenity)
          # We could have used extend() list method too,
          # but would have needed another way to code also
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

  def delete(self, obj=None):
    if obj != None:
      self.__session,delete(obj)

  def reload(self):
      """
      Commit all changes in database after
      the changings
      """
      Base.metadata.create_all(self.__engine)
      session_factory = sessionmaker(
          bind=self.__engine, expire_on_commit=False)
      Session = scoped_session(session_factory)
      self.__session = Session

  def close(self):
        """close session, proper ending"""
        self.__session.remove()

  def classes(self):
        """ returns dictionary of valid classes """
