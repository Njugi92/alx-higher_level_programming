#!/usr/bin/python3
"""It defines a JSON-to- an object function"""
import json


def from_json_string(my_str):
    """This returns a python object representation of a
    JSON string
    """
    return (json.loads(my_str))
