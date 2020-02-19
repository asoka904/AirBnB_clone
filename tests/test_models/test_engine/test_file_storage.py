#!/usr/bin/python3
"""Test File Storage"""
import unittest
import models.engine
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime


class TestFileStorage(unittest.TestCase):
    """Start test"""

    def test_doc00(self):
        """test docstring for module"""
        msg = "Module has not docstring"
        self.assertIsNotNone(models.engine.file_storage.__doc__, msg)

    def test_doc01(self):
        """test docstring for class"""
        msg = "Class has not docstring"
        self.assertIsNotNone(models.engine.file_storage.FileStorage.__doc__, msg)

    def test_doc02(self):
        """test docstring for methods"""
        msg = "all method has not docstring"
        self.assertIsNotNone(models.engine.file_storage.FileStorage.all.__doc__, msg)
        msg = "new method has not docstring"
        self.assertIsNotNone(models.engine.file_storage.FileStorage.new.__doc__, msg)
        msg = "save method has not docstring"
        self.assertIsNotNone(models.engine.file_storage.FileStorage.save.__doc__, msg)
        msg = "reload method has not docstring"
        self.assertIsNotNone(models.engine.file_storage.FileStorage.reload.__doc__, msg)

    def test_instance00(self):
        """test instance"""
        storage = FileStorage()
        self.assertIsInstance(storage, FileStorage)

    def test_instance01(self):
        """test instance is equal"""
        storage1 = FileStorage()
        storage2 = FileStorage()
        self.assertNotEqual(storage1, storage2)

    def test_new00(self):
        """test new00"""
        storage = FileStorage()
        my_dict = dict({
            'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
            'created_at': '2017-09-28T21:03:54.052298',
            '__class__': 'BaseModel',
            'my_number': 89,
            'updated_at': '2017-09-28T21:03:54.052302',
            'name': 'Holberton'
        })
        base = BaseModel(**my_dict)
        storage.new(base)
        key = "BaseModel" + "." + my_dict['id']
        self.assertIn(key, storage.all())

    def test_save00(self):
        """test save00"""
        storage = FileStorage()
        my_dict = dict({
            'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
            'created_at': '2017-09-28T21:03:54.052298',
            '__class__': 'BaseModel',
            'my_number': 89,
            'updated_at': '2017-09-28T21:03:54.052302',
            'name': 'Holberton'
        })
        base = BaseModel(**my_dict)
        storage.new(base)
        storage.save()

    def test_reload00(self):
        """test reload00"""
        storage = FileStorage()
        my_dict = dict({
            'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
            'created_at': '2017-09-28T21:03:54.052298',
            '__class__': 'BaseModel',
            'my_number': 89,
            'updated_at': '2017-09-28T21:03:54.052302',
            'name': 'Holberton'
        })
        key = "BaseModel" + "." + my_dict['id']
        self.assertIn(key, storage.all())
        base = BaseModel(**my_dict)
        storage.new(base)
        storage.save()
        storage.reload()
        self.assertIn(key, storage.all())
