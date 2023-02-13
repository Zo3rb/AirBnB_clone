#!/usr/bin/python3
"""Contains the class BaseModel"""
import uuid
from datetime import datetime


class BaseModel:
    """Defines all common attributes/methods for other sub-classes"""

    def __init__(self, *args, **kwargs):
        """Creates a class instance"""
        from models import storage

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "id":
                    self.id = value
                elif key == "created_at":
                    value = datetime.fromisoformat(value)
                    self.created_at = value
                elif key == "updated_at":
                    value = datetime.fromisoformat(value)
                    self.updated_at = value
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """Returns the formatted str representation of an obj"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the public instance attribute updated_at"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dict containing all keys/values of __dict__ of the
        instance.
        In addition a key __class__ is added with class name as value"""
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()

        return obj_dict
