#!/usr/bin/python3
"""Entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Define the behavior of the command interpreter"""

    prompt = '(hbnb) '
    __models = ['BaseModel']

    def preloop(self):
        """Load the objects in the storage"""
        #self.storage = FileStorage()
        #self.storage.reload()

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Called when an empty line is entered"""
        return ''

    def do_EOF(self, line):
        """EOFCommand to exit the program"""
        return True

    def do_create(self, line):
        """Creates a new instance of a model and saves it"""
        cmd_class = self.check_class(line)
        if cmd_class:
            model = BaseModel()
            storage.new(model)
            storage.save()
            print(model.id)

    def do_show(self, line):
        """prints the string representarion of an model instance"""
        cmd_class = self.check_class(line)
        cmd_id = self.check_id(line)

        if cmd_class and cmd_id:
            results = storage.all()
            key = cmd_class + "." + cmd_id
            if key in results:
                print(results[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Destroys an isntance of a model"""
        key = self.check_class_id(line)

        if key:
            results = storage.all()
            if key in results:
                del results[key]
                storage.save()
            else:
                print("** no instance found **")
    def do_all(self, line):
        """Shows all instances"""
        commands = line.split()
        results = storage.all()
        if len(commands) == 0:
            print([str(values) for values in results.values()])
        elif commands[0] in self.__models:
            print([str(values) for key, values in results.items() if commands[0] in jey])

    def check_class(self, line):
        """Check if the class called exist"""
        commands = line.split()
        if len(commands) > 0:
            if commands[0] in self.__models:
                return commands[0]
            else:
                print("** class doesn't exist **")
                return None
        else:
            print("** class name missing **")
            return False

    def check_id(self, line):
        """Check the command arg"""
        commands = line.split()
        if len(commands) > 1:
            return commands[1]
        print("** instance id missing **")
        return None

    def check_class_id(self, line):
        cmd_class = self.check_class(line)
        cmd_id = self.check_id(line)

        if cmd_class and cmd_id:
            key = cmd_class + "." + cmd_id
            return key
        else:
            return None

if __name__ == "__main__":
    HBNBCommand().cmdloop()
