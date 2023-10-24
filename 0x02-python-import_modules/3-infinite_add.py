#!/usr/bin/python3

if __name__ == "__main__":

    from sys import argv

    if len(argv) - 1 == 0:
        print("0")

    else:
        sum = 0
        for b in range(len(argv) - 1):
            add = int(argv[b + 1])
            sum += add

        print("{:d}".format(sum))

"""
When the program is run directly by the Python interpreter.
"""
