#!/usr/bin/python3
"""
This module define the Place class
"""
import uuid
from datetime import datetime
from models.base_model import BaseModel


class Place(BaseModel):
    """Define the attributes of the Place class"""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Create (or load) a new Place"""
        super().__init__(self, *args, **kwargs)
