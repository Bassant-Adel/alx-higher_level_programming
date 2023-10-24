#!/usr/bin/python3
""" DIVISIBLE """


def divisible_by_2(my_list=[]):
    is_list_divisible_by_2 = []

    for em in my_list:
        if em % 2 == 0:
            is_list_divisible_by_2.append(True)

        else:
            is_list_divisible_by_2.append(False)

    return is_list_divisible_by_2
