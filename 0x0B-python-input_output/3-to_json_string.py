#!/usr/bin/python3
# 3-to_json_string.py
# simon tagbor <simontgbor360@gamil.com>
"""A program to serialize a list into a json string"""


import json


def to_json_string(my_obj):
    """create a json string from a given object
    Args: my_obj - a data structure like a dictionary or a list

    Returns:
            A Json string
    """
    return json.dumps(my_obj)
