#!/usr/bin/python3
"""
This module define the City class
"""
import uuid
from datetime import datetime
from models.base_model import BaseModel


class City(BaseModel):
    """Define the attributes of the City class"""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Create (or load) a new City"""
        super().__init__(self, *args, **kwargs)
