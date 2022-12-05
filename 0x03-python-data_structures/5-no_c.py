#!/usr/bin/python3
# 5-no_c.py
# Simon Tagbor <simontagbor360@gmail.com>

def no_c(my_string):
    wit_noc = ""
    for ch in list(my_string):
        if ch not in 'cC':
            wit_noc += ch
    return (wit_noc)
