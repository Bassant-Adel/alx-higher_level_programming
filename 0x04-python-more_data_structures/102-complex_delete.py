#!/usr/bin/python3
""" KEYS """


def complex_delete(a_dictionary, value):
    for cc in list(a_dictionary):
        if value == a_dictionary.get(cc):
            del a_dictionary[cc]
    return (a_dictionary)
