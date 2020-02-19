#!/usr/bin/python3
"""
This module define the User class
"""

import uuid
from datetime import datetime
from models.base_model import BaseModel


class User(BaseModel):
    """Define the attributes of the User class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Create (or load) a new User"""
        super().__init__(self, *args, **kwargs)
