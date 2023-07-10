#!/usr/bin/python3
"""Dfine function to add atribute to objects"""


def add_attribute(obj, att, value):
    """Adds atribue to object
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
