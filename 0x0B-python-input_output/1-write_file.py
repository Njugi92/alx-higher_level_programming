#!/usr/bin/python3
"""This defines a file-writting function"""


def write_file(filename="", text=""):
    """It writes a string to file UTF8
    Args:
        filename (str): name of the file to write
        text (str): text to write to file
    Return:
        number of character written
    """
    with open(filename, "w", encoding="utf8") as f:
        return (f.write(text))
