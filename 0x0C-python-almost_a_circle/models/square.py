#!/usr/bin/python3
"""
    This module contains a class Square that implements a class Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        A class representing a square.
    """
def __init__(self, size, x=0, y=0, id=None):
    """
    Initializes a Square object.
    Args:
        size (int): The size of the square.
        x (int): The x-coordinate of the square.
        y (int): The y-coordinate of the square.
        id (int): The ID of the square.
    """
    super().__init__(size, size, x, y, id)

@property
def size(self):
    """
    Returns the size of the square.
    """
    return self.width

@size.setter
def size(self, value):
    """
    Sets the size of the square.
    Args:
        value (int): The value to set the size to.
    Raises:
        TypeError: If value is not an integer.
        ValueError: If value is less than or equal to 0.
    """
    if type(value) != int:
        raise TypeError("size must be an integer")
    if value <= 0:
        raise ValueError("size must be > 0")

    self.width = value
    self.height = value

def update(self, *args, **kwargs):
    """
    Updates the square's attributes.
    Args:
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.
    """
    if len(args) == 0:
        for key, val in kwargs.items():
            self.__setattr__(key, val)
        return

    try:
        self.id = args[0]
        self.size = args[1]
        self.x = args[2]
        self.y = args[3]
    except IndexError:
        pass

def __str__(self):
    """
    Returns a string representation of the square.
    """
    return "[{}] ({}) {}/{} - {}".format(type(self).__name__,
                                         self.id, self.x, self.y,
                                         self.width)

def to_dictionary(self):
    """
    Returns the dictionary representation of the square.
    """
    return {'id': getattr(self, "id"),
            'size': getattr(self, "width"),
            'x': getattr(self, "x"),
            'y': getattr(self, "y")}