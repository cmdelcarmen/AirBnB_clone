#!/usr/bin/python3
'''unittests for our FileStorage class found in models/base_model.py
'''
import os
import models
import json
import unittest
from time import sleep
from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    '''unittests for our FileStorage class, testing: __init__(), save(),
    all(), reload(), and attributes from the class.
    '''

    def tearDown(self):
        '''deletes file used to reload objs'''
        try:
            os.remove("file.json")
        except:
            pass

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
        test_obj = storage.all()
        self.assertEqual(dict, type(test_obj))

    def test_reload(self):
        '''Testing the reload method and the __object attr'''
        test_obj = BaseModel()
        models.storage.new(test_obj)
        models.storage.save()
        models.storage.reload()
        dict_ = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + test_obj.id, dict_)

    def test_all2(self):
        '''Testing all() method'''
        test_obj = FileStorage()
        dict_ = test_obj.all()
        self.assertTrue(isinstance(dict_, dict))

    def test_save(self):
        '''Testing save'''
        my_model = BaseModel()
        created = test_obj.updated_at
        sleep(2)
        my_model.save()
        updated = test_obj.updated_at
        self.assertLess(created, updated)

    def test_save(self):
        '''Testing the save method'''
        test_obj = BaseModel()
        test_obj2 = FileStorage()
        models.storage.new(test_obj)
        models.storage.save()
        file_string = ""
        with open("file.json", 'r+') as jfile:
            file_string = jfile.read()
            self.assertIn("BaseModel.", file_string)

    def test_new(self):
        '''Testing the new method'''
        test_obj = BaseModel()
        test_obj2 = FileStorage()
        test_obj2.new(test_obj)
        self.assertNotEqual(test_obj2.all(), 0)

    def test_reload2(self):
        '''Testing the reload method'''
        test_obj = BaseModel()
        test_storage = FileStorage()
        test_obj.name = "Holberton"
        test_obj.save()
        test_storage._FileStorage__objects = {}
        test_storage.reload()
        self.assertNotEqual(test_storage.all(), {})

    def test_save3(self):
        '''Testing save method, testing that a file is created'''
        test_obj = BaseModel()
        test_storage = FileStorage()
        test_obj.save()
        self.assertTrue(os.path.isfile("file.json"))

    def test_save4(self):
        '''Testing save method'''
        test_obj = BaseModel()
        test_obj.name = "Holberton"
        storage = FileStorage()
        test_obj.save()
        with open('file.json', 'r+') as f:
            test_dict = json.load(f)
        value_dict = test_dict.get("BaseModel.{}".format(test_obj.id))
        self.assertEqual(value_dict['name'], "Holberton")

    def test_save5(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)


if __name__ == '__main__':
    unittest.main()
