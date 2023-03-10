#!/usr/bin/python3
"""defines a class Square"""


class Square():
    """represents a square"""
    def __init__(self, size=0):
        """Initializes a square
        Args:
            size (int): size of the square
        """
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
