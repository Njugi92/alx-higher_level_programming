#!/usr/bin/python3
"""It defines a JSON file reading function"""
import json


def load_from_json_file(filename):
    """This creates a python object from a JSON file"""
    with open(filename) as f:
        return (json.load(f))
