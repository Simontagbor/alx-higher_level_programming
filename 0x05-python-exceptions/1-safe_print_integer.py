#!/usr/bin/python3
# 1-safe_print_integer.py
# Simon Tagbor <simontagbor360@gmail.com>

def safe_print_integer(value):
    """prints integer value  with specfied format
    args
    value : value to be printed
    """

    try:
        print("{:d}".format(value))
    except ValueError:
        return False
    else:
        return True
