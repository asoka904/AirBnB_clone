#!/usr/bin/python3
"""Entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Define the behavior of the command interpreter"""

    prompt = '(hbnb) '
    __models = ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place',
                'Review']
    __methods = ['all()', 'count()', 'show()', 'destroy()', 'update()']

    def preloop(self):
        """Load the objects in the storage"""
        pass

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
            model = eval(cmd_class)()
            storage.new(model)
            storage.save()
            print(model.id)

    def do_show(self, line):
        """prints the string representarion of an model instance"""
        key = self.check_class_id(line)

        if key:
            results = storage.all()
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
        """Shows all instances or specific ones"""
        commands = line.split()
        results = storage.all()
        if len(commands) == 0:
            print([str(values) for values in results.values()])
        else:
            if commands[0] in self.__models:
                print([str(values) for key, values in results.items() if
                      commands[0] in key])
            else:
                print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an istance"""
        key = self.check_class_id(line)

        if key:
            results = storage.all()
            if key in results:
                att_val = self.check_attribute_value(line)
                if att_val:
                    setattr(results[key], att_val[0], att_val[1])
                    storage.save()
            else:
                print("** no instance found **")

    def check_class(self, line):
        """Check if the class exists"""
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
        """Check if the id exits"""
        commands = line.split()
        if len(commands) > 1:
            return commands[1]
        print("** instance id missing **")
        return None

    def check_class_id(self, line):
        """Check the class and id exits"""
        cmd_class = self.check_class(line)
        if cmd_class:
            cmd_id = self.check_id(line)
            if cmd_id:
                key = cmd_class + "." + cmd_id
                return key
            else:
                return None

    def check_attribute_value(self, line):
        """Check if the attribute and the value exists"""
        commands = line.split()
        if len(commands) > 2:
            if len(commands) > 3:
                return (commands[2], commands[3])
            else:
                print("** value missing **")
                return None
        else:
            print("** attribute name missing **")
            return None

    def default(self, line):
        """When the command is not recognized"""
        cmds = line.split(".")
        if len(cmds) > 1:
            if cmds[0] in self.__models:
                results = storage.all()
                if cmds[1] == "all()":
                    self.do_all(cmds[0])
                    return
                if cmds[1] == "count()":
                    print(len([str(v) for k, v in results.items()
                          if cmds[0] in k]))
                    return

                s = str(cmds[1][:5]) + str(cmds[1][-1])
                key = cmds[1][6:-2]
                if s == "show()":
                    self.do_show(cmds[0] + " " + key)
                    return

                s = str(cmds[1][:8]) + str(cmds[1][-1])
                key = cmds[1][9:-2]
                if s == "destroy()":
                    self.do_destroy(cmds[0] + " " + key)
                    return

                s = str(cmds[1][:7]) + str(cmds[1][-1])
                if s == "update()":
                    cm = cmds[1].split("{")
                    if len(cm) > 1:
                        key = cmds[0] + "." + cm[0][8:-3]
                        d = "{" + cm[1][:-2] + "}"
                        d = d.replace('\'', '"')
                        my_dict = eval(d)
                        if key in results:
                            for k, v in my_dict.items():
                                setattr(results[key], k, v)
                        else:
                            print("** no instance found **")
                        return
                    else:
                        cm = cmds[1].split("\"")
                        if len(cm) == 1:
                            print("** instance id missing **")
                            return
                        elif len(cm) <= 3 and cm[1] == "":
                            print("** instance id missing **")
                            return
                        elif len(cm) <= 5:
                            print("** value missing **")
                            return
                        else:
                            u = cmds[0] + " " + cm[1] + " " + cm[3] + " "
                            u += cm[5]
                            self.do_update(u)
                            return

        print("Unknown syntax: {}".format(line))

if __name__ == "__main__":
    HBNBCommand().cmdloop()
