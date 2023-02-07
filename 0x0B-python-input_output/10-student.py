#!/usr/bin/python3

"""Defines a class Student"""


class Student:
    """A Student class"""

    def __init__(self, first_name, last_name, age):
        """Initializes a Student obj
        Args:
            first_name (str): first name of student
            last_name (str): last name of student
            age (int): age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves dictionary representation of a Student
        If attrs is a list of strings, only attribute names
        contained in this list are retrieved.
        Args:
            attrs (list): attributes to retrieve
        """
        if type(attrs) == list:
            if all(type(elem) == str for elem in attrs):
                return {key: getattr(self, key)
                        for key in attrs if hasattr(self, key)}
        return (self.__dict__)
