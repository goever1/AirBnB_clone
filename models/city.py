#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

class City(BaseModel):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    state_id = Column(String(60), nullable=False, Foreignkey("states.id")
    name = Column(String(128), nullable=False)
