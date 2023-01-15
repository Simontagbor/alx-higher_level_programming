#!/usr/bin/python3
# rectangle.py
# Simon Tagbor <simontagbor360@gmail.com>
"""A module to implement a subclass Rectangle of Base class"""

from models.base import Base


class Rectangle(Base):
    """define constructor"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.set_width(width)
        self.set_height(height)
        self.set_x(x)
        self.set_y(y)
        super().__init__(id)

    def set_width(self, width):
        self.__width = width

    def set_height(self, height):
        self.__height = height

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self.__y = y
