#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if len(argv) < 2:
        print("0 arguments.")
    else:
        if len(argv) == 2:
            print("{:d} argument:".format(1))
        else:
            print("{:d} arguments:".format(len(argv) - 1))
        for i in range(1, len(argv)):
            print("{:d}: {:s}".format(i, argv[i]))
