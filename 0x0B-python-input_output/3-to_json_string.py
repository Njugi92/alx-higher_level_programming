#!/usr/bin/python3
"""This defines a string to JSON function"""
import json


def to_json_string(my_obj):
    """It returns a JSON representation of a string object"""
    return (json.dumps(my_obj))
