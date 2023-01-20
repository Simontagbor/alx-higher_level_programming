#!/usr/bin/python3
# base.py
# Simon Tagbor <simontagbor360@gmail.com>
"""This  module implements a base class"""


import json


class Base(object):
    """set private variables"""
    __nb_objects = 0

    """define constructor"""
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns a JSON string of list of dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns a list from json string"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save json string to file"""
        filename = "{}.json".format(cls.__name__)

        with open(filename, "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write(json.loads("[]"))
            else:
                dicts = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(dicts))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attribute set
        Args:
            dictionary (dict): a dictionary of attributes
        Returns:
            a new instance of either Rectangle or Square
        """
        if dictionary and dictionry != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """returns a list of instances
        Arg:
            cls (class instance): the class instance of Rectangle or Square

        Returns: a list  of instances
        """
        filename = "{}.json".format(cls.__name__)
        with open(filename, "r", encoding="utf-8") as f:
            if FileNotFoundError:
                return []
            else:
                list_dicts = Base.from_json(f.read())
                return [cls.create(**d) for d in list_dicts]
