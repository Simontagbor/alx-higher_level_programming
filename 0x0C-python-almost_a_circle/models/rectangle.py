#!/usr/bin/python3
# rectangle.py
# Simon Tagbor <simontagbor360@gmail.com>
"""A module to implement a subclass Rectangle of Base class"""

from models.base import Base
import json


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
        if width < 0:
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
        if height < 0:
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

    def area(self):
        """define public area property for rectangle """
        return (self.width * self.height)

    def display(self):
        """Display rectangle using # """
        for i in range(self.y):
            print("")
        for i in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            print("{}".format(self.width * "#"))

    def update(self, *args, **kwargs):
        """Assign an argument to each attribute

        Args:
            args(int): non-keyworded arguments used in update
            kwargs(int): used in assigning keyword arguments.
        """

        if args and len(args) != 0:
            count = 0
            for arg in args:
                if count == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif count == 1:
                    self.width = arg
                elif count == 2:
                    self.height = arg
                elif count == 3:
                    self.x = arg
                elif count == 5:
                    self.y = arg
                count += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                if key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns a dictionary represntaion of a rectangle"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """specify string method for rectangle class"""
        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                self.id, self.x, self.y,
                                                self.width, self.height)
