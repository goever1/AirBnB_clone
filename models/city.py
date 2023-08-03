#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

class City(BaseModel):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
<<<<<<< HEAD
    places = relationship("Place", backref="cities", cascade="delete")
=======
>>>>>>> 4ff267333be7a5f325a76a9bf56474034877cd23
