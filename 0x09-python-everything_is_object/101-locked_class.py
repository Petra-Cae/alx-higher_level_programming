#!/usr/bin/python3
"""
Prevents creation of dynamic new instance attributes
"""


class LockedClass():
    """prevents new dynamic attribute creation"""
    __slots__ = ['first_name']

    def __init__(self):
        """ Init """
        pass
