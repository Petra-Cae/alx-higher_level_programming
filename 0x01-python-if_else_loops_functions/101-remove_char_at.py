#!/usr/bin/python3
"""
    Copies a string and removes the char at nth position
"""


def remove_char_at(str, n):
    """
    Creates a copy of a string, removing the character at position n
    """
    if n < 0:
        return (str)
    return (str[:n] + str[n+1:])
