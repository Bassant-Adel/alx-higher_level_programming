#!/usr/bin/python3
""" KEYS """


def multiply_by_2(a_dictionary):
    n_dictionary = a_dictionary.copy()
    for dd in n_dictionary:
        n_dictionary[dd] = n_dictionary[dd] * 2
    return (n_dictionary)
