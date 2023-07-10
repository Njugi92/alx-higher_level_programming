#!/usr/bin/python3
"""It defines an inherited list class MyList"""


class MyList(list):
    """This impliments sorted printing of built-in list class"""
    def print_sorted(self):
        """It prints a list in sorted asscending order"""
        print(sorted(self))
