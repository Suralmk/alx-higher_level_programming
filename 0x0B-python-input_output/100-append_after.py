#!/usr/bin/python3
"""This module defines a content file insertion function"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts content after each line containing a given string in a file
    """
    content = ""
    with open(filename) as r:
        for line in r:
            content += line
            if search_string in line:
                content += new_string
    with open(filename, "w") as w:
        w.write(content)
