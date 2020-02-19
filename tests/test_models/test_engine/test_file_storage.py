#!/usr/bin/python3
"""Test File Storage"""
import unittest
import models
from models.engine.file_storage import FileStorage
from datetime import datetime
import os


class TestFileStorage(unittest.TestCase):
    """Start test"""

    def test_doc00(self):
        """test docstring for module"""
        msg = "Module has not docstring"
        self.assertIsNotNone(models.engine.file_storage.__doc__, msg)

    def test_doc01(self):
        """test docstring for class"""
        msg = "Class has not docstring"
        doc = FileStorage.__doc__
        self.assertIsNotNone(doc, msg)

    def test_doc02(self):
        """test docstring for methods"""
        msg = "all method has not docstring"
        function = FileStorage.all.__doc__
        self.assertIsNotNone(function, msg)

        msg = "new method has not docstring"
        function = FileStorage.new.__doc__
        self.assertIsNotNone(function, msg)

        msg = "save method has not docstring"
        function = FileStorage.save.__doc__
        self.assertIsNotNone(function, msg)

        msg = "reload method has not docstring"
        function = FileStorage.reload.__doc__
        self.assertIsNotNone(function, msg)

    def test_file00(self):
        """test the file permissions"""
        path = 'tests/test_models/test_engine/test_file_storage.py'
        is_readable = os.access(path, os.R_OK)
        self.assertTrue(is_readable)

        is_executable = os.access(path, os.X_OK)
        self.assertTrue(is_executable)

        is_writable = os.access(path, os.W_OK)
        self.assertTrue(is_writable)

    def test_file01(self):
        """test the file permissions"""
        path = 'models/engine/file_storage.py'
        is_readable = os.access(path, os.R_OK)
        self.assertTrue(is_readable)

        is_executable = os.access(path, os.X_OK)
        self.assertTrue(is_executable)

        is_writable = os.access(path, os.W_OK)
        self.assertTrue(is_writable)

    def test_instance00(self):
        """test instance"""
        storage = FileStorage()
        self.assertIsInstance(storage, FileStorage)
