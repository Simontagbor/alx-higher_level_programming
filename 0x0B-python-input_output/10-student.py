#!/usr/bin/python3
# 10-student.py
# Simon Tagbor <simontagbor360@gmail.com>
"""Create a Class  Student"""


class Student(object):

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        """retrieve the dictionary representation of a Student instance"""
        if (type(attrs) == list and
            all(type(ele) == str for ele in attrs)):
            return {key: getattr(self, key) for key in attr if hasattr(self, key)}
        return self.__dict__
