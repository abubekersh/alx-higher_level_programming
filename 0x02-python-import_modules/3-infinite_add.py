#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    sum = 0
    for i in range(1, len(argv)):
        num = int(argv[i])
        sum = sum + num
    print("{:d}".format(sum))
