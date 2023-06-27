#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    """Excecute a function safely.
    Args:
    fct: Function to excecute.
    args: The arguments for fct
    Returns:
    If an error occurs - None
    Otherwise - The results of the call of fct
    """
    try:
        result = fct(*args)
        return (result)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
