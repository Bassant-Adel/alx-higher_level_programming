#!/usr/bin/python3
""" Square """


class Square:
    """ SSSSquare """

    def __init__(self, size=0):
        """ IIInit """

        self.__size = size

    @property
    def size(self):
        """ SSSize """

        return self.__size

    @size.setter
    def size(self, value):

        if not isinstance(value, int):
            raise TypeError('size must be an integer')

        if value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    def area(self):
        """ R Area """

        return self.__size ** 2

    def __le__(self, other):
        return self.area() <= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __eq__(self, other):
        return self.area() == other.area()
