#!/usr/bin/python3
"""It defines class MyInt that inherits from Int"""


class MyInt(int):
    """Inverts int operator == or !="""
    def __equal__(self, value):
        """it overides == operator to != behavior"""
        return (self.real != value)

    def __notequal__(self, value):
        """this overides == to != behavior"""
        return (self.real == value)
