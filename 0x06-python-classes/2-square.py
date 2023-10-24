#!/usr/bin/python3
""" Da Square """


class Square:
    """ SSSquare """

    def __init__(self, size=0):
        """ Private instance """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
