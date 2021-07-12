#!/usr/bin/python3
'''File defines class HBNBCommand class, the entry point of the
command interpreter.'''

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage


all_classes_dict = {'BaseModel': BaseModel, 'User': User}


class HBNBCommand(cmd.Cmd):
    '''Entry point to command line interpreter.
    '''

    prompt = '(hbnb) '

    @staticmethod
    def check_if_valid_class(class_name):
        '''
        Method checks if class name is valid.
        '''
        if class_name not in all_classes_dict:
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
            if command in all_classes_dict:
                new_instance = all_classes_dict[command]()
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
        cmd_arg[0] = command, cmd_arg[1] = id
        '''
        if command:
            cmd_args = command.split(' ')

            if (HBNBCommand.check_if_valid_class(cmd_args[0])):
                    if len(cmd_args) == 1:
                        print('** instance id missing **')

                    else:
                        if (HBNBCommand.check_if_valid_id(cmd_args[0], cmd_args[1])):
                            print(storage.all()["{}.{}".format(cmd_args[0], cmd_args[1])])
        else:
            print('** class name missing **')

    def do_destroy(self, command):
        '''
        'Destroy' command deletes an instance based on the class
        name and id.
        Example: (hbnb) destroy BaseModel 1234-1234-1234
        '''
        if command:
            cmd_args = command.split(' ')

            if (HBNBCommand.check_if_valid_class(cmd_args[0])):
                    if len(cmd_args) == 1:
                        print('** instance id missing **')

                    else:
                        if (HBNBCommand.check_if_valid_id(cmd_args[0], cmd_args[1])):
                            del storage.all()["{}.{}".format(cmd_args[0], cmd_args[1])]
                            storage.save()
        else:
            print('** class name missing **')

    def do_all(self, command):
        '''
        'All' command prints all string representations of all instances
        based or not on the class name.
        Example: 'all BaseModel' or 'all
        '''
        if command:
            if HBNBCommand.check_if_valid_class(command):
                for key, value in storage.all().items():
                    if value.__class__.__name__ == command:
                        print(str(value))
        else:
            for key, value in storage.all().items():
                print(str(value))

    def do_update(self, command):
        '''
        'Update' command updates an instance based on the class name and id
        by adding or updating attribute.
        Example:(hbnb)update BaseModel 1234-1234-1234 email
            "aibnb@holbertonschool.com
        Usage: update <class name> <id> <attribute name> "<attribute value>""
        '''

        if command:
            cmd_args = command.split(' ')

            if HBNBCommand.check_if_valid_class(cmd_args[0]):
                if len(cmd_args) == 1:
                    print('** instance id missing **')

                else:
                    if HBNBCommand.check_if_valid_id(cmd_args[0], cmd_args[1]):
                        if len(cmd_args) == 2:
                            print('** attribute name missing **')

                        elif len(cmd_args) == 3:
                            print('** value missing **')

                        else:
                            obj = storage.all()["{}.{}".format(cmd_args[0], cmd_args[1])]
                            setattr(obj, cmd_args[2], cmd_args[3].strip('"'))
                            obj.save()
        else:
            print('** class name missing **')

if __name__ == '__main__':
    HBNBCommand().cmdloop()
