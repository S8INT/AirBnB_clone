#!/usr/bin/env python3
"""A class that serializes instances to a JSON file and decerializes them back
"""
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """A class that serializes and deserializes JSON file objects"""

    def __init__(self):
        """The init function to initialize the FileStorage class"""
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj
            self.save()

    def save(self):
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(my_dict, f)

    def delete(self, obj=None):
        """A method that deletes an instance if it's inside attribute
        __objects"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            if (key, obj) in self.__objects.items:
                self.__objects.pop(key, None)
        self.save()

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                my_reload_dict = json.load(f)
                for key, value in (my_reload_dict.items()):
                    self.__objects[key] = eval(value["__class__"])(**value)
        else:
            pass
