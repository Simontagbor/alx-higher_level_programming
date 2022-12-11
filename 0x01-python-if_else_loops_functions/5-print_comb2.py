#!/usr/bin/python3
# 5-print_comb2.py
# Simon Tagbor <simontagbor360@gmail.com>
for number in range(0, 100):
    if number == 99:
        print("{}".format(number))
    else:
        print("{:02}".format(number), end=", ")
