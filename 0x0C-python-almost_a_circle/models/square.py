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

    def update(self, *args, **kwargs):
        """update instance attributes using arguments

        Args:
            args (int): The list of non-keyworded arguments
            kwargs (int): a list of keyworded arguments
        """

        if args and len(args) != 0:
            count = 0
            for count in range(len(args)):
                for arg in args:
                    if count == 0:
                        self.id = arg
                    if count == 1:
                        self.size = arg
                    if count == 2:
                        self.x = arg
                    if count == 3:
                        self.y = arg
                    count += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Return the dictionary representation of the Square instance"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """specify string method for rectangle class"""
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                             self.id, self.x, self.y,
                                             self.size)
