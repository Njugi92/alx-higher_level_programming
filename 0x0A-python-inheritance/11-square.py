#!/usr/bin/python3
"""It defines a rectangle subclass square"""


class Square(Rectangle):
    """Represents a square"""
    def __init__(self, size):
        """Initializes a new square
        Args:
            size (int): size of the new square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
