#!/usr/bin/python3


def magic_calculation(a, b):

    result = 0

    for zz in range(1, 3):
        try:

            if zz > a:
                raise Exception('Too far')
            else:
                result += a ** b / zz

        except Exception:
            result = b + a
            break
    return result
