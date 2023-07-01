#!/usr/bin/python3


def say_my_name(first_name, last_name=""):
    """Print a name.
    Args:
        first_name (str): First name to be printed
        second_name (str): Last name to be printed
    Raises:
        TypeError: if either of first_name or last_name is not strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
