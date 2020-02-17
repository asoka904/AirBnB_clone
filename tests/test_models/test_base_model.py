#!usr/bin/python3

import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):

    def test_init00(self):
        base = BaseModel()

    def test_init01(self):
        base = BaseModel()
        self.assertEqual(base.__class__.__name__, "BaseModel")

    def test_init02(self):
        my_dict = dict({
            'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
            'created_at': '2017-09-28T21:03:54.052298',
            '__class__': 'BaseModel',
            'my_number': 89,
            'updated_at': '2017-09-28T21:03:54.052302',
            'name': 'Holberton'
        })
        base = BaseModel(**my_dict)
        self.assertEqual(base.id, '56d43177-cc5f-4d6c-a0c1-e167f8c27337')

    def test_init03(self):
        my_dict = dict({
            'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
            'created_at': '2017-09-28T21:03:54.052298',
            '__class__': 'BaseModel',
            'my_number': 89,
            'updated_at': '2017-09-28T21:03:54.052302',
            'name': 'Holberton'
        })
        base = BaseModel(**my_dict)
        self.assertEqual(base.created_at, datetime.strptime('2017-09-28T21:03:54.052298', "%Y-%m-%dT%H:%M:%S.%f"))

    def test_init04(self):
        my_dict = dict({
            'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
            'created_at': '2017-09-28T21:03:54.052298',
            '__class__': 'BaseModel',
            'my_number': 89,
            'updated_at': '2017-09-28T21:03:54.052302',
            'name': 'Holberton'
        })
        base = BaseModel(**my_dict)
        self.assertEqual(base.updated_at, datetime.strptime('2017-09-28T21:03:54.052302', "%Y-%m-%dT%H:%M:%S.%f"))

    def test_init05(self):
        my_dict = dict({
            'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
            'created_at': '2017-09-28T21:03:54.052298',
            '__class__': 'BaseModel',
            'my_number': 89,
            'updated_at': '2017-09-28T21:03:54.052302',
            'name': 'Holberton'
        })
        base = BaseModel(**my_dict)
        self.assertEqual(base.my_number, 89)

    def test_init06(self):
        my_dict = dict({
            'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
            'created_at': '2017-09-28T21:03:54.052298',
            '__class__': 'BaseModel',
            'my_number': 89,
            'updated_at': '2017-09-28T21:03:54.052302',
            'name': 'Holberton'
        })
        base = BaseModel(**my_dict)
        self.assertEqual(base.name, 'Holberton')
