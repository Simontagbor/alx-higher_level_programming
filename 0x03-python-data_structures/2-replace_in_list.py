#!/usr/bin/python3
# 2-replace_in_list.py
# Tagbor Simon <simontagbor360@gmail.com>

""" A function to replace a list element at a given index """


def replace_in_list(my_list, idx, element):
    if idx >= 0 and idx < (len(my_list)):
        my_list[idx] = element
    return (my_list)
