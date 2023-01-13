#!/usr/bin/python3
# 7-base_geometry.py
# Simon Tagbor <simontagbor360"gmail.com">
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Represent base geometry."""
    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        self.name = name
        self.value = value
        """Return True if  Value is an integer
        Args:
            name is always a string
            value is always an int
        """
        if not isinstance(self.value, int):
           raise TypeError("{} must be an integer".format(self.name))
        elif self.value <= 0:
            raise ValueError("{} must be greator than 0".format(self.name))
