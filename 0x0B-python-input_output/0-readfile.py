# 0-readfile.py
# Auth: Simon Tagbor <simontagbor360@gmail.com>
""" This Program displays the contents of a file """


def read_file(filename=""):
    """This function accepts a string representing the filename
    Args:
        filename is a string representing the name of file.
    Return:
        all file contents
    """
    with open(filename, "r") as f:
        print(f.read(), end="")
