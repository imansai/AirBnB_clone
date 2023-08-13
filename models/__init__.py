#!/usr/bin/python3
"""Instantiates a distinct FileStorage object for your application."""
from models.engine.file_storage import FileStorage

"""Variable storage that holds an instance of the FileStorage class."""
storage = FileStorage()
storage.reload()
