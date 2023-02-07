#!/usr/bin/python3

"""
Returns JSON representation of an object
"""


import json


def to_json_string(my_obj):
    """Converts an object to JSON
    Args:
        my_obj: object to be converted
    Return:
        string representation of the object
    """
    return json.dumps(my_obj)
