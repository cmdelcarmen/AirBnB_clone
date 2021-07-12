#!/usr/bin/python3
'''Defines User class that inherits from BaseModel'''


from models.base_model import BaseModel


class User(BaseModel):
    '''User class inherits from BaseModel. Attributes:
    email: User's email.
    password: User's password.
    first_name: User's first name.
    last_name: User's last name.
    '''

    email = ""
    password = ""
    first_name = ""
    last_name = ""
