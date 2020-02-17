#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '

    def do_quit(self, arg):
        'Quit command to exit the program'
        return True

    def emptyline(self):
        return ''

    def do_EOF(self, line):
        'EOF command to exit the program'
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
