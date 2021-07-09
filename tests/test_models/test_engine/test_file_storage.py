#!/usr/bin/python3
'''unittests for our FileStorage class found in models/base_model.py
'''
import os
import models
import unittest
from time import sleep
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    '''unittests for our FileStorage class, testing: __init__(), save(),
    all(), reload(), and attributes from the class.
    '''
    def test_file_path(self):
        '''Testing the __file_path attribute from FileStorage by attempting
        to delete the file it is supposed to create, file.json.
        '''
        test_obj = BaseModel()
        test_obj.id = "1"
        test_obj.save()
        try:
            os.remove("file.json")
        except:
            pass

    def test_objects(self):
        '''Testing the __objects attribute from FileStorage,
        making sure it is type dict
        '''
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_all(self):
        '''Testing the all method of FileStorage, making sure it returns
        the dictionary.
        '''
        test_obj = FileStorage()
        self.assertEqual(dict, type(test_obj.all()))

    def test_reload(self):
        '''Testing the reload method and the __object attr'''
        test_obj = BaseModel()
        models.storage.new(test_obj)
        models.storage.save()
        models.storage.reload()
        dict_ = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + test_obj.id, dict_)

if __name__ == '__main__':
    unittest.main()
