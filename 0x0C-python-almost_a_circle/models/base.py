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
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
