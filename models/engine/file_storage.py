#!/usr/bin/python3
"""
Manage the storage of every object
"""
import json
import os
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User


class FileStorage:
    """Serializes instances to a JSON file"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj"""
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        new_obj = {}
        with open(self.__file_path, 'w') as f:
            for k, v in self.__objects.items():
                new_obj[k] = v.to_dict()
            f.write(json.dumps(new_obj))

    def reload(self):
        """reload method"""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as f:
                results = f.read()
                if results is not "":
                    my_json = json.loads(results)
                    for k, v in my_json.items():
                        cls = eval(v["__class__"])(**v)
                        self.__objects[k] = cls
