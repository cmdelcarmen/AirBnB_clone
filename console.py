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

    def emptyline(self):
        '''Handles no input'''
        pass

    def do_quit(self, command):
        ''''Quit' command exits program.\n'''
        return True

    def do_EOF(self, command):
        ''''EOF' command exits program.\n'''
        print()
        return True

    def do_create(self, command):
        ''''Create' command creates a new instance of Basemodel,
        saves it (to the JSON file) and prints the id.
        Example: (hbnb) create BaseModel'''
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
        ''''Show' command prints the string representation of an
        instance based on the class name and the id.
        Example: (hbnb) show BaseModel 1234-1234-1234'''
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
        ''''Destroy' command deletes an instance based on the class
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
                object_dict = storage.all()

                if "{}.{}".format(cmd_args[0], cmd_args[1]) in obj_dict:
                    del obj_dict["{}.{}".format(cmd_args[0], cmd_args[1])]
                    storage.save()
                else:
                    print('** no instance found **')
            else:
                print('** class doesn\'t exist **')

if __name__ == '__main__':
    HBNBCommand().cmdloop()
