#!/usr/bin/python3
# 1-write_file.py
# Simon Tagbor <simontagbor360@gmail.com>
""" A program to write a string to a text file """


def write_file(filename="", text=""):
    """update file with given text
    Args: [Filename] a string for the name of file to be written
          [text] a specified text to be written to the file.
    Returns:
            the number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
        return len(list(text))
