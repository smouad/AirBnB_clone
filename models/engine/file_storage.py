#!/usr/bin/python3
import json


class FileStorage:
    __file_path = "file.json"
    __object = dict()

    def all(self):
        return FileStorage.__object

    def new(self, obj):
        FileStorage.__object['{}.{}'.format(obj.__class__, obj.__id)] = {}

    def save(self):
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(FileStorage.__object, f)

    def reload(self):
        try:
            f = open(FileStorage.__file_path)
        except Exception:
            pass
        else:
            FileStorage.__object = json.load(f)
