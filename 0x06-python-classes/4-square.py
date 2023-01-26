!/usr/bin/python3
"""class Square"""


class Square():
    """reps a square"""

    def __init__(self, size=0):
        """Initialize a square
        Args:
            size (int): size of the square
        """
        self.__size = size

    @property
    def size(self):
        """gets/sets the current square size"""
        return self.__size

    @size.setter
    def size(self, value):
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the area of the square"""
        return (self.__size * self.__size)
