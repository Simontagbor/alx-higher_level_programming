#!/usr/bin/python3
# test_base.py
# Simon Tagbor <simontagbor360@gmail.com>
"""unittest for the Base class"""
from models.base import Base
import unittest

class TestBase(unittest.TestCase):
    """Test basic attributes and properties of the base class"""

    def SetUp(self):
        pass

    def testID(self):
        self.base1 = Base()
        self.assertEqual(self.base1.id, 1, "incorrect id")
        self.base2 = Base()
        self.assertEqual(self.base2.id, 2, "incorrect id")
        self.base3 = Base()
        self.assertEqual(self.base3.id, 3, "incorrect id")
        self.base4 = Base(12)
        self.assertEqual(self.base4.id, 12, "incorrect id")
        self.base5 = Base()
        self.assertEqual(self.base5.id, 4, "incorrect id")

if __name__ == "__main__":
    unittest.main()
