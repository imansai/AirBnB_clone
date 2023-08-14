#!/usr/bin/python3
"""Instantiates a unique FileStorage object tailored for the application."""
from models.engine.file_storage import FileStorage

"""A variable storage, which holds an instance of FileStorage"""
storage = FileStorage()
storage.reload()
