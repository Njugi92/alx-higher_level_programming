#!/usr/bin/python3
"""This defines a class checking function"""


def is_same_class(obj, a_class):
    """It checks if an object is an instance of given class
    Args:
        obj (any): Object to check
        a_class (type): class to match the type of obj to.
    Returns:
        if obj is an instance of a_class - True
        otherwise - False
    """
    if type(obj) == a_class:
        return (True)
    return (False)
