#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    # executes a function safely
    try:
        result = fct(*args)
    except Exception as unsafe:
        sys.stderr.write("Exception: {}\n".format(unsafe))
        result = None
    return (result)
