#!/usr/bin/python3
"""It defines a class student"""


class Student:
    """A representation of student"""
    def __init__(self, first_name, last_name, age):
        """It is initialization of new student
        Args:
            first_name (str): first name of student
            last_name (str): last name of student
            age (int): age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """It gets a dictionary representation of student
        if attrs is list of strings, rep only those
        attributes included in the list.
        Args:
            attrs (list): attributes to represent
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return (self.__dict__)

    def reload_from_json(self, json):
        """It replaces all attributes of student
        Args:
            json (dict): keys/value pairs to replace attribute with
        """
        for k, v in json.items():
            setattr(self, k, v)
