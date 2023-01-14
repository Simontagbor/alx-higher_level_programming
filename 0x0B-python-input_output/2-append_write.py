#!/usr/bin/python3
# 2-append_write.py
# Simon  Tagbor <simontagbor360@gmail.com>
""" A program to append a string to a file """


def append_write(filename="", text=""):
    """append a file with a specified text
    Args:
        filename - the name of the file must be a string
        text - the text to be appended, also a string type

    Returns:
        the number of characters written
    """
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
        return len(list(text))
