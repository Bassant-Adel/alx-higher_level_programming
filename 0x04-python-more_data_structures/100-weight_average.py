#!/usr/bin/python3
""" KEYS """


def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    lis1 = sum(map(lambda ml: ml[0] * ml[1], my_list))
    lis2 = sum(map(lambda ml: ml[1], my_list))
    return lis1 / lis2
