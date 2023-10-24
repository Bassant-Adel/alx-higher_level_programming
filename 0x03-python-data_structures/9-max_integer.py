#!/usr/bin/python3
""" MAX """


def max_integer(my_list=[]):

    if len(my_list) == 0:
        return None
    max = my_list[0]

    for em in my_list:
        if em > max:
            max = em
    return max
