#!/usr/bin/python3
"""It defines a locked class"""


class LockedClass:
    """prevents the user from instntiating a neww LockedClass attribute
    for anything but attributes called 'first_name'
    """
    __slots__ = ["first_name"]
