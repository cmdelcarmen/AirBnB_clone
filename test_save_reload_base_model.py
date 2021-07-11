#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

all_objs = storage.all()
if len(all_objs) == 0:
    print("hi")
print(all_objs)
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
        obj = all_objs[obj_id]
        print(obj)

print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "Holberton"
my_model.my_number = 89
my_model.save()
for obj_id in all_objs.keys():
        obj = all_objs[obj_id]
        print(obj)
