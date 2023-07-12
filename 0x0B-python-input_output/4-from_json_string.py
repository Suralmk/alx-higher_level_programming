#!/usr/bin/python3
"""defines a JSON-to-object function"""


import json


def from_json_string(my_str):
    """Python object representation of a JSON string is returned"""
    return json.loads(my_str)
