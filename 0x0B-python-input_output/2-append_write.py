#!/usr/bin/python3
"""The function appends a file"""


def append_write(filename="", text=""):
    """Appends a string to the end of UTF8 text file
    Args:
        filename (str): This is name of file to append to
        text (str): the string to append to a file
    Return:
        Number of character appended
    """
    with open(filename, "a", enconding="utf8") as f:
        return (f.write(text))
