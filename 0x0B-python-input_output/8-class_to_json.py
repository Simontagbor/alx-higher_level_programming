#!/usr/bin/python3
# 8-class_to_json
# Simon Tagbor <simontagbor360@gmail.com>
"""Serialize the class description of a class instance"""


def class_to_json(obj):
    """Create dictionary containing the class description of an instance"""
    return obj.__dir__
