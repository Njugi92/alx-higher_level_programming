#!/usr/bin/python3
def no_c(my_string):
    """Remove all characters c and C from a string."""
    copy = [k for k in my_string if k != 'c' and k != 'C']
    return ("".join(copy))
