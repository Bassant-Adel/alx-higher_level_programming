#!/usr/bin/python3
""" Square """


class Square:
    """ SSSquare """

    def __init__(self, size=0):
        """ IIInit """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """ AAArea """
        return self.__size ** 2

    @property
    def size(self):
        """ SSSize """
        return self.__size

    @size.setter
    def size(self, value):
        """ SSSize """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value
