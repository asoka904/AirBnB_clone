#!/usr/bin/python3
"""
This module define the Review class
"""
import uuid
from datetime import datetime
from models.base_model import BaseModel


class Review(BaseModel):
    """Define the attributes of the Review class"""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Create (or load) a new Review"""
        super().__init__(self, *args, **kwargs)
