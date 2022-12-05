#!/usr/bin/python3
# 8-multiple_returns.py
# Simon Tagbor <simontagbor360@gmail.com>


def multiple_returns(sentence):
    """Returns the length of a string and its first character."""
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
