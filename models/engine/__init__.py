#!/usr/bin/python3
"""Instantiate a unique FileStorage object for your application"""
from models.engine.file_storage import FileStorage

"""Create a storage variable, which holds an instance of FileStorage"""
storage = FileStorage()
storage.reload()
