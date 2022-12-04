#!/usr/bin/python3
# 3-print_alphabt.py
# Simon Tagbor Gabriel K <simontagbor360@gmail.com>

"""Print the alphabet in lowercase, not followed by a new line."""
for letter in range(97, 123):
    if chr(letter) not in 'eq':
        print("{}".format(chr(letter)), end="")
