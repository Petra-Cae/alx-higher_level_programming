#!/usr/bin/python3
# checks for lowercase characters


def islower(c):
    if ord(c) > 96 and ord(c) < 123:
        return True
    else:
        return False
