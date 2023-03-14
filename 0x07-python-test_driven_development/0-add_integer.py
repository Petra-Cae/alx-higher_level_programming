""" Function for adding two integers """


def add_integer(a, b=98):
    """ adds integers
        Args:
        @a: first integer
        @b: second integer, sets 98 as default
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)