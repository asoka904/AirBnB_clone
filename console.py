#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '

    def preloop(self):
        self.storage = FileStorage()
        self.storage.reload()

    def do_quit(self, arg):
        'Quit command to exit the program'
        return True

    def emptyline(self):
        return ''

    def do_EOF(self, line):
        'EOF command to exit the program'
        return True

    def do_create(self, line):
        'Creates a new instance of BaseModel and saves it '
        if self.check_class(line):
            base = BaseModel()
            self.storage.new(base)
            self.storage.save()
            print(base.id)

    def do_show(self, line):
        'Prints the string representation of an instance based on the class name and id'
        if self.check_class(line) and self.check_id(line):
            results = self.storage.all()
            if self.check_id(line) in results:
                print(results[self.check_id(line)])
            else:
                print("** no instance found **")
        
    def check_class(self, line):
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
        commands = line.split()
        if len(commands) >= 2:
            return commands[1]
        print("** instance id missing **")
        return False

if __name__ == "__main__":
    HBNBCommand().cmdloop()
