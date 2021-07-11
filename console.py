#!/usr/bin/python3
'''File defines class HBNBCommand class, the entry point of the
command interpreter.'''

import cmd
import models


class HBNBCommand(cmd.Cmd):
    '''Entry point to command line interpreter.
    'quit' and EOF should exit program.
    'ENTER' + empty line should not execute anything.
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
