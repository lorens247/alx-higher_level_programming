#!/usr/bin/python3
"""
The 4-print_square module supplies one function, print_square(size).
"""

def print_square(size):
    """
    This function prints a square made up of '#' characters with a side length of size.

    Args:
        size (int): The side length of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.

    Returns:
        None
    """

    # Check that size is an integer
    if type(size) is not int:
        raise TypeError("size must be an integer")

    # Check if size is greater than or equal to 0
    if size < 0:
        raise ValueError("size must be >= 0")

    # If size is greater than 0, print the square
    if size > 0:
        # Use the multiplication operator to create a string of '#'s with a length of 'size'
        # Multiply the above string with '\n' to create the rows of the square
        # Finally, multiply the above result with 'size' to create the square
        print(("#" * size + "\n") * size, end="")
