#!/usr/bin/python3
""" """
import models
from os import getenv
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.user import User
from sqlalchemy.exc import OperationalError


class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ """
        new = self.value()
        self.assertNotEqual(type(new.first_name), int)

    def test_last_name(self):
        """ """
        new = self.value()
        self.assertNotEqual(type(new.last_name), int)

    def test_email(self):
        """ """
        new = self.value()
        self.assertNotEqual(type(new.email), int)

    def test_password(self):
        """ """
        new = self.value()
        self.assertNotEqual(type(new.password), int)

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db', "not supported")
    def test_without_mandatory_arguments(self):
        """Check for mandatory arguments """
        new = self.value()
        with self.assertRaises(OperationalError):
            try:
                new.save()
            except Exception as error:
                models.storage._DBStorage__session.rollback()
                raise error

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') == 'db', "not supported")
    def test_is_subclass(self):
        """Check that State is a subclass of Basemodel"""
        self.assertTrue(isinstance(self.user, User))
