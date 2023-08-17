#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='states', cascade='all, delete')
    
    @property
    def cities(self):
        """getter attribute to return list of City instances"""
        from models import storage
        from models.city import City
         city_dict = models.storage.all(City)
            city_list = []
            for key, value in city_dict.items():
                if value.state_id == self.id:
                    city_list.append(value)
            return city_list
