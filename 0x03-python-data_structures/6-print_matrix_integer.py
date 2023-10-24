#!/usr/bin/python3
""" PRINT """


def print_matrix_integer(matrix=[[]]):

    for ss in matrix:
        for xx in ss:
            print("{:d}".format(xx), end=" " if xx != ss[-1] else "")
        print()
