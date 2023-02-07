#!/usr/bin/python3
"""Defines a class-to-JSON function"""


def class_to_json(obj):
    """Returns the dictionary representation of a simple data struct
    Args:
        obj (object): a simple data structure
    Return:
        Dictionary representation of object
    """
    return (obj.__dict__)
