#!/usr/bin/python3
"""represents a square"""


class Square():
    """square with size and position"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square
        Args:
            size (int): size of the square
            position(tuple): squares's position
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """"gets/sets the size of the square"""
        return self.__size

    @property
    def position(self):
        """"gets/sets the square's position"""
        return self.__position

    @size.setter
    def size(self, value):
        """"gets/sets the size of the square"""
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """"gets/sets the square's position"""
        if (type(value) is not tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (type(value[0]) is not int) or (type(value[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (value[0] < 0) or (value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """"returns the area of the square"""
        return (self.size * self.size)

    def my_print(self):
        """prints out the square"""
        if self.__size == 0:
            print("")
            return

        for y in range(self.__position[1]):
            print("")

        for y in range(self.__size):
            for x in range(self.__position[0]):
                print(" ", end="")
            for z in range(self.__size):
                print("#", end="")
            print("")
