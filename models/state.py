#!/usr/bin/python3
"""
This module define the State class
"""
import uuid
from datetime import datetime
from models.base_model import BaseModel


class State(BaseModel):
    """Define the attributes of the State class"""

    name = ""

    def __init__(self, *args, **kwargs):
        """Create (or load) a new State"""
        super().__init__(self, *args, **kwargs)
