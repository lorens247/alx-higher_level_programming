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
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer or float')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer or float')

    return int(a) + int(b)
