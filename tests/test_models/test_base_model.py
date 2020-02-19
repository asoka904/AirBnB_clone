#!usr/bin/python3
"""Test BaseModel"""
import unittest
import models
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Start test"""

    def test_doc00(self):
        """test docstring for module"""
        msg = "Module has not docstring"
        self.assertIsNotNone(models.base_model.__doc__, msg)

    def test_doc01(self):
        """test docstring for class"""
        msg = "Class has not docstring"
        self.assertIsNotNone(models.base_model.BaseModel.__doc__, msg)

    def test_doc02(self):
        """test docstring for methods"""
        msg = "__init__ method has not docstring"
        self.assertIsNotNone(models.base_model.BaseModel.__init__.__doc__, msg)
        msg = "__str__ method has not docstring"
        self.assertIsNotNone(models.base_model.BaseModel.__str__.__doc__, msg)
        msg = "__save__ method has not docstring"
        self.assertIsNotNone(models.base_model.BaseModel.save.__doc__, msg)
        msg = "__to_dict__ method has not docstring"
        self.assertIsNotNone(models.base_model.BaseModel.to_dict.__doc__, msg)

    def test_instance00(self):
        """test isntance"""
        base = BaseModel()
        self.assertIsInstance(base, BaseModel)

    def test_instance01(self):
        """test instance is equal"""
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertNotEqual(base1, base2)

    def test_init00(self):
        """test init instantiation"""
        base = BaseModel()

    def test_init01(self):
        """test init class name"""
        base = BaseModel()
        self.assertEqual(base.__class__.__name__, "BaseModel")

    def test_init02(self):
        """test init id"""
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
        """test init created at"""
        my_dict = dict({
            'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
            'created_at': '2017-09-28T21:03:54.052298',
            '__class__': 'BaseModel',
            'my_number': 89,
            'updated_at': '2017-09-28T21:03:54.052302',
            'name': 'Holberton'
        })
        base = BaseModel(**my_dict)
        self.assertEqual(base.created_at, datetime.strptime(
                    '2017-09-28T21:03:54.052298', "%Y-%m-%dT%H:%M:%S.%f"))

    def test_init04(self):
        """test init updated at"""
        my_dict = dict({
            'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
            'created_at': '2017-09-28T21:03:54.052298',
            '__class__': 'BaseModel',
            'my_number': 89,
            'updated_at': '2017-09-28T21:03:54.052302',
            'name': 'Holberton'
        })
        base = BaseModel(**my_dict)
        self.assertEqual(base.updated_at, datetime.strptime(
                    '2017-09-28T21:03:54.052302', "%Y-%m-%dT%H:%M:%S.%f"))

    def test_init05(self):
        """test init my_number"""
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
        """test init name"""
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

    def test_init07(self):
        """test init check datetime"""
        base = BaseModel()
        self.assertIsInstance(base.created_at, datetime)
        self.assertIsInstance(base.updated_at, datetime)

    def test_save00(self):
        """test updated_at"""
        base = BaseModel()
        updated_at1 = base.updated_at
        base.save()
        updated_at2 = base.updated_at
        self.assertNotEqual(updated_at1, updated_at2)

    def test_to_dict00(self):
        """test to_dict method return"""
        base = BaseModel()
        self.assertIsInstance(base.to_dict(), dict)

    def test_to_dict01(self):
        """test to_dict method class key"""
        base = BaseModel()
        self.assertIn('__class__', base.to_dict())

    def test_to_dict02(self):
        """test is date is in isoformat"""
        base = BaseModel()
        base_dict = base.to_dict()
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)
