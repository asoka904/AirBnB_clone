#!/usr/bin/python3
"""Test File Storage"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime


class TestFileStorage(unittest.TestCase):
    """Start tests"""

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
        self.assertIn(my_dict['id'], storage.all())

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
        self.assertIn(my_dict['id'], storage.all())
        base = BaseModel(**my_dict)
        storage.new(base)
        storage.save()
        storage.reload()
