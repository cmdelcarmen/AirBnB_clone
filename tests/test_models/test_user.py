#!/usr/bin/python3
'''Unittest for User class in models/user.py'''

import unittest
from datetime import datetime
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    '''Unittest for User class'''

    def test_user_init(self):
        '''Testing that an instance is created'''
        test_obj = User()
        self.assertIsInstance(test_obj, User)

    def test_user_attrs(self):
        '''Testing User inherits from BaseModel'''
        test_obj = User()
        self.assertTrue(isinstance(test_obj, BaseModel))

    def test_user_id(self):
        '''Testing the id attr'''
        test_obj = User()
        self.assertEqual(type(test_obj.id), str)

    def test_user_created_and_updated_at(self):
        '''Testing created_at and updated at attrs'''
        test_obj = User()
        self.assertEqual(type(test_obj.created_at), datetime)
        self.assertEqual(type(test_obj.updated_at), datetime)

    def test_user_str(self):
        '''Testing __str__ method'''
        test_obj = User()
        test_obj.email = "yay@yay.com"
        test_obj_str = test_obj.__str__()
        self.assertIn("User", test_obj_str)
        self.assertIn("email", test_obj_str)
        self.assertIn("yay@yay.com", test_obj_str)

    def test_BaseModelAttr(self):
        '''Testing User() attrs'''
        self.assertTrue(hasattr(User, "email"))
        self.assertTrue(hasattr(User, "password"))
        self.assertTrue(hasattr(User, "first_name"))
        self.assertTrue(hasattr(User, "last_name"))

if __name__ == '__main__':
        unittest.main()

