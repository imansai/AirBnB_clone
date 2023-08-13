#!/usr/bin/python3
"""Class inheritance from the BaseModel class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Representing a class User"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
