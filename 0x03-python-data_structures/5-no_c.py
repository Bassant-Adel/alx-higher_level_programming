#!/usr/bin/python3
""" NO """


def no_c(my_string):
    no_c_string = ""

    for ss in my_string:
        if ss != 'c' and ss != 'C':
            no_c_string += ss

    return no_c_string
