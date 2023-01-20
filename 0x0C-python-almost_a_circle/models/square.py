#!/usr/bin/python3
# square.py
# Simon Tagbor <simontagbor360@gmail.com>
"""Implement a Square Class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """represent a class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialise a new square

        Args:
            size (int): the size of square instance
            x (int): The x cordinate of a square.
            y (int): The y coordinate of a sqare instance
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get or set the value for size of the square"""
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def __str__(self):
        """specify string method for rectangle class"""
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                             self.id, self.x, self.y,
                                             self.size)
