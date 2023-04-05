#!/usr/bin/python3
"""LockedClass module."""


class LockedClass:
    """LockedClass class containing  only __slots__."""
    __slots__ = ['first_name']

    def __setattr__(self, name, value):
        """Set the value of an attribute."""
        if name == "first_name":
            self.__dict__[name] = value
        else:
            raise AttributeError("'LockedClass' object has no attribute '" + name + "'")
