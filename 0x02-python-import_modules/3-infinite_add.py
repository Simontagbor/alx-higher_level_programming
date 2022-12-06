#!/usr/bin/python3
# 3-infinite_add.py
# Simon Tagbor <simontagbor360@gmail.com>

if __name__ == "__main__":
    import sys
    result = 0
    for i in range(len(sys.argv) - 1):
        result += int(sys.argv[i+1])
    print("{:d}".format(result))
