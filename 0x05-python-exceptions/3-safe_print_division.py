#!/usr/bin/python3


def safe_print_division(a, b):
    zz = 0

    try:
        zz = a / b

    except ZeroDivisionError:
        zz = None
    finally:
        print("Inside result: {}".format(zz))
    return zz
