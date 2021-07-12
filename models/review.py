#!/usr/bin/python3
'''Defines Review class that inherits from BaseModel'''


from models.base_model import BaseModel


class Review(BaseModel):
    '''Review class inherits from BaseModel. Attributes:
    place_id (str): The id of the Place.
    user_id (str): The id of the User.
    text (str): ""
    '''
    place_id = ""
    user_id = ""
    text = ""
