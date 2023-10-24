#!/usr/bin/python3
""" Square """


class Square:
    """ SSSquare """

    def __init__(self, size=0):
        """
            Private
            instance
        """
        self.size = size

    @property
    def size(self):
        """ SSSize """
        return self.__size

    @size.setter
    def size(self, value):
        """ SSSize """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """ AAArea """
        return self.__size * self.__size

    def my_print(self):
        """ PPPrint """

        for i in range(self.size):
            print("#" * self.size)

        if self.size == 0:
            print()
