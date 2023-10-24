#!/usr/bin/python3
""" KEYS """


def print_sorted_dictionary(a_dictionary):
    for dd in sorted(a_dictionary.keys()):
        print("{:s}: {}".format(dd, a_dictionary.get(dd)))
