#!/usr/bin/python3
"""It defines a class Student"""


class Student:
    """This represents student"""
    def __init__(self, first_name, last_name, age):
        """it initializes new student
        Args:
            first_name (str): first name of the student
            last_name (str): last name of the student
            age (int): age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """This gets dictionary representation of Student"""
        return (self.__dict__)
