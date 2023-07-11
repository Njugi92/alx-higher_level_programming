#!/usr/bin/python3
"""It defines class Rectangle which inherits from
BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """It represents a rectangle using BaseGeometry"""
    def __init__(self, width, height):
        """Initializes a new Rectangle
        Args:
            width (int): width of a new rectangle
            height (int): height of new rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
