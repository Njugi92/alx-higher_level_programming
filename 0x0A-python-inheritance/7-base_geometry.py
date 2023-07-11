#!/usr/bin/python3
"""Defines a BaseGeometry class"""


class BaseGeometry:
    """It represents a base geometry"""
    def area(self):
        """Not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """It validates a parimeter as an integer
        Args:
            name (str): validates name as parimeter
            value (int): parimeter to validate
        Raises:
            TypeError: if value is not an integer
            ValueError: if the value is <= 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
