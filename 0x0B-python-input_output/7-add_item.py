#!/usr/bin/python3
# 7-add_item.py
# Simon  Tagbor <simontagbor360@gmail.com>
""" create a list from all arguments """
import sys


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        arguments = load_from_json_file("add_item.json")
    except FileNotFoundError:
        arguments = []
    arguments.extend(sys.argv[1:])
    save_to_json_file(arguments, "add_item.json")
