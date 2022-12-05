#!/usr/bin/python3
# 4-new_in_list.py
# Simon Tagbor <simontagbor360@gmail.com>

def new_in_list(my_list, idx, element):
    """a function to replace an element of a list"""
    new_list = my_list.copy()
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)

    new_list[idx] = element
    return (new_list)
