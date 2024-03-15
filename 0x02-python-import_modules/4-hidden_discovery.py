#!/usr/bin/python3.8
import hidden_4
if __name__ == "__main__":
    for i in dir(hidden_4):
        if (i[0] == "_" and i[1] == "_"):
            continue
        else:
            print(i)
