#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        for zz in range(x):
            print(my_list[zz], end="")
        print()
        return x

    except IndexError:

        print()
        return zz
