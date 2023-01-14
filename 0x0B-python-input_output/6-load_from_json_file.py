#!/usr/bin/python3
# 6-load_from_json_file.py
# Simon Tagbor <simontagbor360@gmail.com>
"""Create Object from a json file"""


import json


def load_from_json_file(filename):
    """Load the contents of JSON file and create an object"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.loads(f.read())
