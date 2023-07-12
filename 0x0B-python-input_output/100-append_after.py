#!/usr/bin/python3
"""This defines a text file insertion function"""


def append_after(filename="", search_string="", new_string=""):
    """it inserts text after each line containing a given string
    in a file
    Args:
        filename (str): name of the file
        search_string (str): string to search for within a file
        new_string (str): string to inseart
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
