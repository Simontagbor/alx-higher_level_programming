#!/usr/bin/python3
# 4-from_json_string.py
# simon tagbor <simontgbor360@gamil.com>
"""A program to decode a json string and return an object"""


import json


def to_json_string(my_str):
    """create an from a given jsonstring
    Args: my_str - a JSON string

    Returns:
            a data object
    """
    return json.loads(my_str)
