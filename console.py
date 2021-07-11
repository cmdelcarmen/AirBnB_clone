#!/usr/bin/python3
'''File defines class HBNBCommand class, the entry point of the
command interpreter.'''

import cmd
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    '''Entry point to command line interpreter.
    '''

    prompt = '(hbnb) '

    @staticmethod
    def check_if_valid_class(class_name):
        '''
        Method checks if class name is valid.
        '''
        if class_name != 'BaseModel':
            print('** class doesn\'t exist **')
            return False
        else:
            return True

    @staticmethod
    def check_if_valid_id(class_name, obj_id):
        '''
        Method checks if instance id is valid.
        '''
        if "{}.{}".format(class_name, obj_id) not in storage.all():
            print('** no instance found **')
            return False
        else:
            return True

    def emptyline(self):
        '''
        Handles no input
        '''
        pass

    def do_quit(self, command):
        '''
        'Quit' command exits program.\n
        '''
        return True

    def do_EOF(self, command):
        '''
        'EOF' command exits program.\n
        '''
        print()
        return True

    def do_create(self, command):
        '''
        'Create' command creates a new instance of Basemodel,
        saves it (to the JSON file) and prints the id.
        Example: (hbnb) create BaseModel
        '''
        if command:
            if command == 'BaseModel':
                new_instance = BaseModel()
                new_instance.save()
                print(new_instance.id)
            else:
                print('** class doesn\'t exist **')

        else:
            print('** class name missing **')

    def do_show(self, command):
        '''
        'Show' command prints the string representation of an
        instance based on the class name and the id.
        Example: (hbnb) show BaseModel 1234-1234-1234
        '''
        cmd_args = command.split(' ')

        if cmd_args == ['']:
            print('** class name missing **')

        elif len(cmd_args) < 2:
            print('** instance id missing **')

        else:
            if cmd_args[0] == 'BaseModel':
                obj_dict = storage.all()

                if "{}.{}".format(cmd_args[0], cmd_args[1]) in obj_dict:
                    print(obj_dict["{}.{}".format(cmd_args[0], cmd_args[1])])
                else:
                    print('** no instance found **')
            else:
                print('** class doesn\'t exist **')

    def do_destroy(self, command):
        '''
        'Destroy' command deletes an instance based on the class
        name and id.
        Example: (hbnb) destroy BaseModel 1234-1234-1234
        '''
        cmd_args = command.split(' ')

        if cmd_args == ['']:
            print('** class name missing **')

        elif len(cmd_args) < 2:
            print('** instance id missing **')

        else:
            if cmd_args[0] == 'BaseModel':
                obj_dict = storage.all()

                if "{}.{}".format(cmd_args[0], cmd_args[1]) in obj_dict:
                    del obj_dict["{}.{}".format(cmd_args[0], cmd_args[1])]
                    storage.save()
                else:
                    print('** no instance found **')
            else:
                print('** class doesn\'t exist **')

    def do_all(self, command):
        '''
        'All' command prints all string representations of all instances
        based or not on the class name.
        Example: 'all BaseModel' or 'all
        '''
        cmd_args = command.split(' ')

        if cmd_args == ['']:
            for key, value in storage.all().items():
                print(str(value))
        elif cmd_args[0] == 'BaseModel':
            for key, value in storage.all().items():
                if value.__class__.__name__ == cmd_args[0]:
                    print(str(value))
        else:
            print('** class doesn\'t exist **')

    def do_update(self, command):
        '''
        'Update' command updates an instance based on the class name and id
        by adding or updating attribute.
        Example:(hbnb)update BaseModel 1234-1234-1234 email
            "aibnb@holbertonschool.com
        Usage: update <class name> <id> <attribute name> "<attribute value>""
        '''
        cmd_args = command.split(' ')

        if cmd_args == ['']:
            print('** class name missing **')

        elif (len(cmd_args) == 1)\
                and HBNBCommand.check_if_valid_class(cmd_args[0]):
            '''Valid class name, but no id passed.'''
            print('** instance id missing **')

        elif (len(cmd_args) == 2)\
                and HBNBCommand.check_if_valid_class(cmd_args[0])\
                and HBNBCommand.check_if_valid_id(cmd_args[0], cmd_args[1]):
            '''Valid class name, valid id, but not attr passed.'''
            print('** attribute name missing **')

        elif (len(cmd_args) == 3)\
                and HBNBCommand.check_if_valid_class(cmd_args[0])\
                and HBNBCommand.check_if_valid_id(cmd_args[0], cmd_args[1]):
            '''Valid class name, valid id, attr passed but no value
            for attr passed.'''
            printf('** value missing **')

        elif (len(cmd_args) >= 4):
            obj = storage.all()["{}.{}".format(cmd_args[0], cmd_args[1])]
            setattr(update_obj, cmd_args[2], cmd_args[3].strip('"'))
            obj.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
