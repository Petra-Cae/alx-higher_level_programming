#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    # prints an integer
    try:
        print("{:d}".format(value))
        return (True)
    except Exception as not_i:
        sys.stderr.write("Exception: {}\n".format(not_i))
        return (False)
