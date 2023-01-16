#!/usr/bin/python3
# rectangle.py
# Simon Tagbor <simontagbor360@gmail.com>
"""A module to implement a subclass Rectangle of Base class"""

from models.base import Base


class Rectangle(Base):
    """define constructor"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """set or get with attribute"""
        return self.__width

    @width.setter
    def width(self, width):
        """Add validation"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        """set or get with attribute"""
        return self.__height

    @height.setter
    def height(self, height):
        """Add validation"""
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        """set or get x cordinatate of rectangle"""
        return self.__x

    @x.setter
    def x(self, x):
        """Add Validation"""
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        """set or get y cordinate of ractangle"""
        return self.__y

    @y.setter
    def y(self, y):
        """Add Validation"""
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y
