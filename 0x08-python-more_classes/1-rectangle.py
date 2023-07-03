#!/usr/bin/python3
"""This is a rectangle class"""


class Rectangle:
    """Representation of a rectangle"""
    def __init__(self, width=0, height=0):
        """Initialization of new rectangle.
        Args:
            width (int): width of a new rectangle
            height (int): height of a new rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """It gets/sets width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """It gets/sets height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
