#!/usr/bin/python3
'''Defines class FileStorage. FileStorage saves all of our
objects created when the programming is running to a file.
'''

import json
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    '''Class serializes instances to a JSON file and
    deserializes JSON file to instances.
    Private class attrs:
        __file_path: A string, the path to the JSON file.
        __objects: A dictionary, stores all objects by
            <class name>.id (ex: to store a BaseModel object with
            id=12121212, the key will be BaseModel.12121212).
    Public instance methods:
        all(self): Returns the dictionary __objects.
        new(self, obj): Sets in __objects the obj with key
            <obj class name>.id
        save(self): Serializes __objects to the JSON file (path: __file_path)
        reload(self): Deserializes the JSON file to __objects (only if the
        JSON file (__file_path) exists; otherwise, does nothing.
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''Returns the dictionary self.__objects.'''
        return self.__objects

    def new(self, obj):
        '''Add the obj to the __objects dictionary with the key:
        <obj class name>.idx
        '''
        key = "{}.".format(obj.__class__.__name__)
        key += "{}".format(obj.id)
        self.__objects[key] = obj

    def save(self):
        '''Serializes the __objects attribute to a JSON file,
        the path is stored in the attribute __file_path variable.

        self.__objects is a dictionary of the actual objects, we use
        a for loop to create a new dictionary that holds the attrs of
        the objects. We call BaseModel's 'to_dict' method, that
        returns a dict of all the attrs of the instance and changes datetime
        attrs into strings before we call the json.dumps method.
        '''
        copy_objects_dict = {}

        for key, value in self.__objects.items():
            copy_objects_dict[key] = value.to_dict()

        with open(self.__file_path, 'w+') as j_file:
            json.dump(copy_objects_dict, j_file)

    def reload(self):
        '''Desrializes the JSON file to __objects. If the file path does not
        exists, no exceptions are raised.
        '''
        try:
            with open(self.__file_path, 'r+') as j_file:
                new_dict = json.load(j_file)
            for key, value in new_dict.items():
                classes = key.split(".")
                self.__objects[key] = eval(classes[0])(**value)

        except:
            pass
