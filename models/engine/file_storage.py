#!/usr/bin/python3
"""
File storage module
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dict __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        Args:
            obj(object): Newly created objected to be added to __objects dict
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        with open(self.__file_path, "w") as fd:
            dict_store = {}
            for k, v in self.__objects.items():
                dict_store[k] = v.to_dict()
            json.dump(dict_store, fd)

    def reload(self):
        """
        Deserializes the JSON file to __objects only if the JSON file
        `__file_path` exists; otherwise do nothing.
        If the file doesn't exist, no exception should be raised
        """
        try:
            with open(self.__file_path) as fd:
                for obj in json.load(fd).values():
                    self.new(eval(obj["__class__"])(**obj))

        except Exception:
            return
