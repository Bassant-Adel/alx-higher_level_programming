#!/usr/bin/python3

if __name__ == "__main__":

    from sys import argv

    if len(argv) - 1 == 0:
        print("0 arguments.")
    elif len(argv) - 1 == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(len(argv) - 1))

    for b in range(len(argv) - 1):
        print("{:d}: {:s}".format(b + 1, argv[b + 1]))

"""
When the program is run directly by the Python interpreter.
"""
