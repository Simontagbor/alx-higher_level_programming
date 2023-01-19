#!/usr/bin/python3
# test_rectangle.py
# Simon Tagbor <simontagbor360@gmail.com>
"""test module for recatangle Class from models.rectangle"""
import sys
import io
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test basic properties and methods of the Rectangle class"""
    def setUp(self):
        self.r1 = Rectangle(10, 2)
        self.r2 = Rectangle(2, 10)
        self.r3 = Rectangle(10, 2, 0, 0, 12)

    def tearDown(self):
        """clean up test cases"""
        del self.r1
        del self.r2
        del self.r3

    def testId(self):
        """test the return value of calling
        id method on an instance of Rectangle
        """
        self.assertEqual(self.r1.id, 5, "unexcpected id value")
        self.assertEqual(self.r2.id, 6, "unexpected id value")
        self.assertEqual(self.r3.id, 12, "unexpected id value")

    def testInteger(self):
        """Test validations against non integers"""
        with self.assertRaises(TypeError) as ctx:
            Rectangle(10, "2")
        err_msg = "height must be an integer"
        self.assertEqual(str(ctx.exception), err_msg)

        with self.assertRaises(ValueError) as ctx:
            Rectangle(-2, 2)
        err_msg = "width must be > 0"
        self.assertEqual(str(ctx.exception), err_msg)

        with self.assertRaises(TypeError) as ctx:
            Rectangle(10, 2, "2", 3)
        err_msg = "x must be an integer"
        self.assertEqual(str(ctx.exception), err_msg)

        with self.assertRaises(ValueError) as ctx:
            Rectangle(5, 2, 7, -3)
        err_msg = "y must be >= 0"
        self.assertEqual(str(ctx.exception), err_msg)

    def testArea(self):
        """Test the area method of the rectangle class"""

        self.assertEqual(self.r1.area(), 20)

    @staticmethod
    def testRectangle_stdout(r, method):
        """Capture the display value of calling
           display on a rectangl instance

        Args:
            r(Rectangle): the rectangle instance to print to stdout
            method(str): the  method to use on the instance r
        Returns:
            string printed to stdout by calling method on r
        """

        capture = io.StringIO()
        sys.stdout = capture

        if method == "print":
            print(r)
        else:
            r.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_Rectangle_display(self):
        r = Rectangle(3, 3, 5, 6, 0)
        r2 = Rectangle(3, 2, 1, 0, 1)
        capture = TestRectangle.testRectangle_stdout(r, "display")
        capture2 = TestRectangle.testRectangle_stdout(r2, "display")
        self.assertEqual("\n\n\n\n\n\n     ###\n     ###\n     ###\n",
                         capture.getvalue())
        self.assertEqual(capture2.getvalue(), " ###\n ###\n")

    def testRecatangle_str_(self):
        """Test the string method of the Rectangle instance"""
        capture = TestRectangle.testRectangle_stdout(self.r3, "print")
        # test print return value
        self.assertEqual(capture.getvalue(),
                         "[Rectangle] (12) 0/0 - 10/2\n")

        # test  __str__ method
        self.assertEqual(self.r3.__str__(),
                         "[Rectangle] (12) 0/0 - 10/2")
