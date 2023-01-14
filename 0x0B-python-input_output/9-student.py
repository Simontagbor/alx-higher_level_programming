#!/usr/bin/python3
# 9-student.py
# Simon Tagbor <simontagbor360@gmail.com>
"""Create a Class  Student"""


class Student(object):

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):

        """retrieve the dictionary representation of a Student instance"""
        return self.__dict__
