#!/usr/bin/python3
# 1-element_at.py
# Simon Tagbor Gabriel <simontagbor360@gmail.com>

"""pretrieve element at a given index"""
def element_at(my_list, idx):
    if idx < 0 or idx > len(my_list):
        return None
    else:
        return my_list[idx]
