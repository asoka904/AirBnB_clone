#!/usr/bin/python3
"""
This module define the Amenity class
"""
import uuid
from datetime import datetime
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Define the attributes of the Amenity class"""

    name = ""

    def __init__(self, *args, **kwargs):
        """Create (or load) a new Amenity"""
        super().__init__(self, *args, **kwargs)
