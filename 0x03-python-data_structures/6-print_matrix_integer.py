#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if (matrix == [[]]):
        print("")
    else:
        for row in matrix:
            for column in row:
                if row.index(column) + 1 == len(row):
                    print("{:d}".format(column))
                else:
                    print("{:d}".format(column), end=" ")
