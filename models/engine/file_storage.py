#!/usr/bin/python3

""" the file storage class """

import json
from models.base_model import BaseModel

class FileStorage:
    """the FileStorate class that stores our data"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns all the stored objects"""
        return self.__objects

    def new(self, obj):
        """save the new object in the objects dict"""
        if obj:
            key = f"{type(obj).__name__}.{obj.id}"
            self.__objects[key] = obj

    def save(self):
        """save the objects dict to the json file"""
        dict_of_objects = {}
        for key, value in self.__objects.items():
            dict_of_objects[key] = value.to_dict()
        objects_str = json.dumps(dict_of_objects)
        with open(self.__file_path, "w") as f:
            f.write(objects_str)

    def reload(self):
        """reads from the json file and stores it in object dict"""
        try:
            f = open(self.__file_path)
        except Exception:
            pass
        else:
            self.__objects = json.load(f)
