#!/usr/bin/python3
"""Manage the storage of every object"""
import json
import os


class FileStorage:
    """Serializes instances to a JSON file"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj"""
        self.__objects[obj.id] = obj.to_dict()

    def save(self):
        """serializes __objects to the JSON file"""
        with open(self.__file_path, 'w') as f:
            f.write(json.dumps(self.__objects))

    def reload(self):
        """reload method"""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as f:
                results = f.read()
                if results is not "":
                    self.__objects = json.loads(results)
