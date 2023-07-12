#!/usr/bin/python3
"""defines a JSON file-writing function"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON format"""
    with open(filename, "w") as format_j:
        json.dump(my_obj, format_j)
