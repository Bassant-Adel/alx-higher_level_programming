#!/usr/bin/python3
""" UNIQ """


def uniq_add(my_list=[]):
    nadd = 0

    for n in set(my_list):
        nadd += n
    return nadd
