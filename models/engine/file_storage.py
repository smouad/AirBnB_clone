#!/usr/bin/python3

import json
from ..base_model import BaseModel
from ..amenity import Amenity
from ..user import User
from ..city import City
from ..state import State
from ..place import Place
from ..review import Review

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        if obj:
            key = f"{type(obj).__name__}.{obj.id}"
            self.__objects[key] = obj

    def save(self):
        dict_of_objects = {}

        for key, value in self.__objects.items():
            dict_of_objects[key] = value.to_dict()
        objects_str = json.dumps(dict_of_objects)
        with open(self.__file_path, "w") as f:
            f.write(objects_str)

    def reload(self):
        try:
            f = open(self.__file_path)
        except Exception:
            pass
        else:
            self.__objects = json.load(f)
