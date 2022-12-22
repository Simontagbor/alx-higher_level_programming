#!/usr/bin/python3
# 0-safe_printt_list
# Simon Tagbor <simontagbor360@gmail.com>

def safe_print_list(my_list=[], x=0):
    """prints x elements of a list.

     Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.
    Returns:
        The number of elements printed.
    """
    num_elmts = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            num_elmts += 1
        except IndexError:
            break
    print("")
    return (num_elmts)
