#!/usr/bin/python3
# 7-islower.py
# SimonTagbor <simontagbor360@gmail.com>


def islower(c):
    " a function to check lower case character """
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
