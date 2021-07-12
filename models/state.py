#!/usr/bin/python3
'''Defines State class that inherits from BaseModel'''


from models.base_model import BaseModel


class State(BaseModel):
    '''State class inherits from BaseModel. Attributes:
    name (str): Name of state.
    '''
    name = ""
