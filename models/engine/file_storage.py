#!/usr/bin/python3
import json
import os
"""Manage the storage of every object"""

class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to
    instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects[obj.id] = obj.to_dict()

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w') as f:
            f.write(json.dumps(self.__objects))

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists; otherwise, do nothing."""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as f:
                results = f.read()
                if results is not "":
                    self.__objects = json.loads(results)
