#!/usr/bin/python3
# oop on a class square


class Square():
    """Class representing a square"""

    def __init__(self, size):
        """ initialize a square

        Args:
           size (int): the size of the square
        """
        self.__size = size
