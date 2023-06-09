#!/usr/bin/python3
def max_integer(my_list=[]):
    """Find the biggest integer of a list."""
    if len(my_list) == 0:
        return (None)
    biggest = my_list[0]
    for k in range(len(my_list)):
        if my_list[k] > biggest:
            biggest = my_list[k]
    return (biggest)
