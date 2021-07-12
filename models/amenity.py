#!/usr/bin/python3
'''Defines Amenity class that inherits from BaseModel'''


from models.base_model import BaseModel


class Amenity(BaseModel):
    '''Amenity class inherits from BaseModel. Attributes:
    name (str): Name of Amenity
    '''
    name = ""
