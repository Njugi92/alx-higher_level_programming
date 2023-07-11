#!/usr/bin/python3
"""This defines a txt reading function"""


def read_file(filename=""):
    """It prints the contents of a UTF8 text file to stdout"""
    with open(filename, encoding="utf8") as f:
        print(f.read(), end="")
