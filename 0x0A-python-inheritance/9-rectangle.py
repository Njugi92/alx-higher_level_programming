#!/usr/bin/python3
"""It defines a class rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """represents a rectangle using base geometry"""
    def __init__(self, width, height):
        """Initializing new rectangle
        Args:
            width (int): width of a new rectangle
            height (int): height of the new rectangle
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """It returns area of the rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """It returns the print() and str() representation of
        rectangle
        """
        string = "[" + str(self, __class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return (string)
