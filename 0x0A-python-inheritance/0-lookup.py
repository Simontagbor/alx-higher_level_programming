#!/usr/bin/python3
# 0-lookup.py
# Simon Tagbor <simontagbor360@gmail.com>

"""Defines an object attribute lookup function."""


def lookup(obj):
    """Returns a list of an object's available attributes and methods"""
    return (dir(obj))
