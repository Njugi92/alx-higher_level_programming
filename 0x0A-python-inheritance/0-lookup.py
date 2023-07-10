#!/usr/bin/python3
"""It defines an object attribute loock up function"""


def lookup(obj):
    """This returns a list of available objects attribute"""
    return (dir(obj))
