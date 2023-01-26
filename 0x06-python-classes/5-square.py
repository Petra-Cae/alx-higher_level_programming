#!/usr/bin/python3
"""defines a class Square"""


class Square():
    """represents a square class"""

    def __init__(self, size=0):
        """Initialize a square
        Args:
            size (int): size of the square
        """
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """gets/sets the size of the square"""
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """ prints out the square with # """
        if not self.__size:
            print("")
        for i in range(self.__size):
            print("#" * self.__size)
        print("")
