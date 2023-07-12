#!/usr/bin/python3
"""It defines a class Student"""


class Student:
    """Representation of student"""
    def __init__(self, first_name, last_name, age):
        """Initializing new student
        Args:
            first_name (str): first name of student
            last_name (str): last name of a student
            age (int): age of a student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """It gets a dictionary representation of student.
        if attrs is a list of strings,rep only those attributes
        in the list
        Args:
            attrs (list): attributes to present
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return (self.__dict__)
