#!/usr/bin/python3


def search_replace(my_list, search, replace):
    """
    A function that repalce an element item
    by another element
    """
    new = []
    for item in my_list:
        if item == search:
            new.append(replace)
        else:
            new.append(item)
    return new
