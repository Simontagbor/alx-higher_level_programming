#!/usr/bin/python3
# 8-islower.py
# SimonTagbor <simontagbor360@gmail.com>


def uppercase(str):
    " a function to check uppercase character """
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print("")
