#!/usr/bin/python3
"""Entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """Define the behavior of the command interpreter"""

    prompt = '(hbnb) '

    def preloop(self):
        """Load the objects in the storage"""
        self.storage = FileStorage()
        self.storage.reload()

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt"""
        return ''

    def do_EOF(self, line):
        """EOFCommand to exit the program"""
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel and saves it"""
        if self.check_class(line):
            base = BaseModel()
            self.storage.new(base)
            self.storage.save()
            print(base.id)

    def do_show(self, line):
        """prints the string representarion of an instance"""
        if self.check_class(line) and self.check_id(line):
            results = self.storage.all()
            if self.check_id(line) in results:
                print(results[self.check_id(line)])
            else:
                print("** no instance found **")

    def check_class(self, line):
        """Check if the class called exist"""
        commands = line.split()
        for i, c in enumerate(commands):
            if i is 0:
                if c == 'BaseModel':
                    return True
                else:
                    print("** class doesn't exist **")
                    return False
        print("** class name missing **")
        return False

    def check_id(self, line):
        """Check the command arg"""
        commands = line.split()
        if len(commands) >= 2:
            return commands[1]
        print("** instance id missing **")
        return False


if __name__ == "__main__":
    HBNBCommand().cmdloop()
