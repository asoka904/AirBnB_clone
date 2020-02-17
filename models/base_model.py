#!/usr/bin/python3
""" This module define the BaseModel class """
import uuid
from datetime import datetime


class BaseModel:

    def __init__(self, *args, **kwargs):
        """Create (or load) a new BaseModel"""
        if kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    if key == "created_at" or key == "updated_at":
                        setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Return a string with attributes of the instance"""
        return "[{}] ({}) {}"\
            .format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the
        instance"""
        my_dict = dict(self.__dict__)
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict
