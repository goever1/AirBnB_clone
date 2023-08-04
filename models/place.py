#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv
import models

env = getenv('HBNB_TYPE_STORAGE')

class Place(BaseModel, Base if (env == "db") else object):
    """ A place to stay """
    if env == 'db':
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", backref="place", cascade="delete")
        amenities = relationship("Amenity", back_populates=place_amenity,
                                 viewonly=False, backref='places')
        place_amenity = Table('place_amenity', Base.metadata,
                                Column('place_id', String(60),
                                       ForeignKey('places.id'),
                                       primary_key=True, nullable=False),
                                Column('amenity_id', String(60),
                                       ForeignKey('amenities.id'),
                                       primary_key=True, nullable=False))

    else:
      
      @property
        def reviews(self):
            """get a list of linked reviews"""
            review_list = []
            for review in list(models.storage.all(Review).values()):
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(selfl):
            """get amenities"""
            amenity_list = []
            for amenity in list(models.storage.all(Amenity).values()):
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, value):
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
