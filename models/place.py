#!/usr/bin/python3
'''Defines Place class that inherits from BaseModel'''


from models.base_model import BaseModel


class Place(BaseModel):
    '''Place class inherits from BaseModel. Attributes:
    city_id (str): The id of the city.
    user_id (str): The id of the User.
    name (str): The name of the place.
    description (str): The description of the place.
    number_rooms (str): .
    number_bathrooms (int): .
    max_guest (int): .
    price_by_night (int): .
    latitude (float): .
    longtitude (float): .
    amenity_ids (list): .
    '''
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
