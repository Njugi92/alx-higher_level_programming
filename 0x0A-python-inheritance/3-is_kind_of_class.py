#!/usr/bin/python3
"""It defines a class and inherited class function"""


def is_kind_of_class(obj, a_class):
    """This checks if object is an instance of instance of
    inherited class.
    Args:
        obj (any): It is object to check
        a_class (type): class to match the type of obj to.
    Return:
        if obj is instance of inherited instance of a_class - True
        otherwise - False
    """
    if isinstance(obj, a_class):
        return (True)
    return (False)
