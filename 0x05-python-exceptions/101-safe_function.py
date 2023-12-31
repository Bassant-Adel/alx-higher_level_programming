#!/usr/bin/python3


def safe_function(fct, *args):

    import sys

    try:
        return fct(*args)
    except Exception as zz:
        print("Exception: {}".format(zz), file=sys.stderr)

        return None
