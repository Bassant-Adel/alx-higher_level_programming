#!/usr/bin/python3
""" KEYS """


def simple_delete(a_dictionary, key=""):
    if key in a_dictionary.keys():
        del a_dictionary[key]
    return a_dictionary
