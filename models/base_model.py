#!/usr/bin/python3
'''File defines the class BaseModel'''

import uuid
from datetime import datetime
import models


class BaseModel:
    '''Class defines all common attributes/methods for other classes.
    Public instance attributes:
        id: A string assigned an uuid when an instance is created.
        created_at: A datetime object assigned the current datetime when
            an instance is created.
        updated_at: A datetime object assigned the current datetime when
            an instance is created, updated every time the object is changed.
    Public instance methods:
        save(self): Updates the public instance attribute updated_at
            with the current datetime.
        to_dict(self): Returns a dictionary containing all keys/values of the
            __dict__ of the instance, self.__dict__ only returns the
            attributes of the instance, so a key __class__ will be added to
            this dictionary paired with the class name of the object.
            'created_at'/'updated_at' will be converted to string objects in
            ISO format(format: %Y-%m-%dT%H:%M:%S.%f
            (ex: 2017-06-14T22:31:03.285259)). This method will be the first
            piece of the serialization/deserialization process: It creates a
            dictionary representation with "simple object type" of our
            BaseModel
        __str__(self): returns the str representation of the instance:
            [<class name>] (<self.id>) <self.__dict__>
    '''
    def __init__(self, *args, **kwargs):
        '''
        id: A string assigned an uuid when an instance is created.
        created_at: A datetime object assigned the current datetime when
            an instance is created.
        updated_at: A datetime object assigned the current datetime when
            an instance is created, updated every time the object is changed.
        '''
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    dt = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, dt)
                else:
                    if key != "__class__":
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        '''Returns the str representation of the instance:
            [<class name>] (<self.id>) <self.__dict__>'''
        c_n = self.__class__.__name__
        return "[{}] ({}) {}".format(c_n, self.id, self.__dict__)

    def to_dict(self):
        '''Returns a dictionary of all the attributes of the BaseModel instance,
        including the class name of the object(key: '__class__').'created_at'/
        'updated_at' will be converted from datetime objects to strings in
        ISO format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)
        '''
        new_dict_copy = self.__dict__.copy()
        new_dict_copy['__class__'] = self.__class__.__name__
        new_dict_copy['created_at'] = self.created_at.isoformat()
        new_dict_copy['updated_at'] = self.updated_at.isoformat()
        return new_dict_copy

    def save(self):
        '''Updates the public instance attribute updated_at to a new datetime object
        '''
        self.updated_at = datetime.utcnow()
        models.storage.save()
