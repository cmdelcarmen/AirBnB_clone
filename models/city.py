#!/usr/bin/python3
'''Defines City class that inherits from BaseModel'''


from models.base_model import BaseModel


class City(BaseModel):
    '''City class inherits from BaseModel. Attributes:
    state_id (str): The id of the state
    name (str): The name of the city
    '''
    state_id = ""
    name = ""
