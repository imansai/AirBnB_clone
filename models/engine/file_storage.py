#!/usr/bin/python3
"""file_storage.py module"""
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage():
    """
    FileStorage class:
    ------------------
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Publicly accessible instance method that
        retrieves the dictionary named "__objects"
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Publicly accessible instance method that adds
        the "obj" to the "__objects" dictionary using
        the key "<obj class name>.id".
        Variables:
        ----------
        key [str] -- key format generated.
        """
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """
        Instance method accessible to the public that
        converts "__objects" dictionary into JSON
        format and saves it to the JSON file
        located at "__file_path".
        Variables:
        ----------
        new_dict [dict] -- keys and values to build JSON.
        """
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict().copy()
        with open(FileStorage.__file_path, mode='w') as my_file:
            json.dump(new_dict, my_file)

    def reload(self):
        """
        Publicly accessible instance method that takes
        JSON file and converts its contents into
        the "__objects" dictionary.
        """
        try:
            with open(FileStorage.__file_path, mode='r') as my_file:
                new_dict = json.load(my_file)

            for key, value in new_dict.items():
                class_name = value.get('__class__')
                obj = eval(class_name + '(**value)')
                FileStorage.__objects[key] = obj

        except FileNotFoundError:
            pass
