#!/usr/bin/python3
# 1-calculations.py
# Simon Tagbor <simontagbor360@gmail.com>


if __name__ == "__main__":
    """simple script to make use of functions"""
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
