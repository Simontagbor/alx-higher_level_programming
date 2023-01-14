#!/usr/bin/python3
# 5-saveto_json_file.py
# Simon Tagbor <simontagbor360@gmail.com>
""" A program that creates a json file and write objects into it """


import json


def save_to_json_file(my_obj, filename):
    """Create ajson file and write a json string into it
    Args:
        my_obj - a data object that gets serialized into a file

        filename - the name of the json file to be created
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
