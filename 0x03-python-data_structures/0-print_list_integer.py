#!/usr/bin/python3
# 0-print_list_integer.py
# Simon Tagbor <simontagbor360@gmail.com>

""" A function to print list of integers """


def print_list_integer(my_list):
    for num in range(len(my_list)):
        print("{:d}".format(my_list[num]))
