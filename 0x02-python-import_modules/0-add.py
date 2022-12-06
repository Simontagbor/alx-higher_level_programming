#!/usr/bin/python3
# 0_dd.py
# Simon Tagbor <simontagbor360@gmail.com>

if __name__ == "__main__":
    """Print the sum  of variables"""
    from add_0 import add

    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
