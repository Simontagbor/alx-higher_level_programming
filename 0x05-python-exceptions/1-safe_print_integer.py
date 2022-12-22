#!/usr/bin/python3
# 1-safe_print_integer.py
# Simon Tagbor <simontagbor360@gmail.com>

def safe_print_integer(value):
    """prints integer value  with specfied format
    Args
        value : value to be printed

    Returns:
        If a TypeError or ValueError occurs - False.
        Otherwise - True.
    """

    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
