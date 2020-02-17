#!/usr/bin/python3
import json
import os

class FileStorage:
    __file_path = ""
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects[obj.id] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w') as f:
            f.write(json.dumps)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file (__file_path)"""
        results = {}
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as f:
                results = json.loads(f.read())
        return results
