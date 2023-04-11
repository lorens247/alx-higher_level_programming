#!/usr/bin/python3

"""
This is the add_integer module.
This module supplies one function, add_integer().
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): The first number to add.
        b (int or float): The second number to add. Defaults to 98.

    Raises:
        TypeError: If a or b is not an integer or float.

    Returns:
        int: The sum of a and b, casted to an integer.
    """
    if type(a) in [int, float]:
        try:
            a = int(a)
        except:
            raise TypeError('a must be an integer')
    else:
        raise TypeError('a must be an integer')

    if type(b) in [int, float]:
        try:
            b = int(b)
        except:
            raise TypeError('b must be an integer')
    else:
        raise TypeError('b must be an integer')

    return a + b
