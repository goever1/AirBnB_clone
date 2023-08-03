#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class State(BaseModel):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

@property
def cities(self):
    from models import storage
    from models.city import City
    cities_list = []
    for city in storage.all(city).values():
        if city.state_id == seld.id:
            cities_list.append(city)
    return cities_list
