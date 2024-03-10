#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return

# #!/usr/bin/python3

# """ the file storage class """

# import json
# from models.base_model import BaseModel

# class FileStorage:
#     """the FileStorate class that stores our data"""
#     __file_path = "file.json"
#     __objects = {}

#     def all(self):
#         """returns all the stored objects"""
#         return self.__objects

#     def new(self, obj):
#         """save the new object in the objects dict"""
#         if obj:
#             key = f"{type(obj).__name__}.{obj.id}"
#             self.__objects[key] = obj

#     def save(self):
#         """save the objects dict to the json file"""
#         dict_of_objects = {}
#         for key, value in self.__objects.items():
#             dict_of_objects[key] = value.to_dict()
#         objects_str = json.dumps(dict_of_objects)
#         with open(self.__file_path, "w") as f:
#             f.write(objects_str)

#     def reload(self):
#         """reads from the json file and stores it in object dict"""
#         try:
#             with open(self.__file_path, "r") as f:
#                 objects_str = f.read()
#             if (objects_str):
#                 json_content = json.loads(objects_str)
#                 for key, value in json_content.items():
#                     class_name = globals()[value.get("__class__")]
#                     self.__objects[key] = class_name(**value)
#         except (FileNotFoundError, FileExistsError):
#             pass
