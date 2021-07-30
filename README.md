# 0x00. AirBnB clone - The console  

Written by Caroline Del Carmen, with some early work done by Jose Vazquez  
in my BaseModel class.  

Project Goals:  

•Put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of our future instances  
•Create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file  
•Create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel  
•Create the first abstracted storage engine of the project: File storage.  
•Create all unittests to validate all our classes and storage engine   

# File Descriptions 
------------  
- models/    
  - base_model.py - Contains class BaseModel that defines all common attributes/methods for other classes.  
- models/engine  
  - file_storage.py - Contains class FileStorage that serializes objects to a JSON file, and deserializes JSON files to a python object.  
- console.py - The entry point of the command interpreter.  
- tests/ - Folder contains all unittests.  
