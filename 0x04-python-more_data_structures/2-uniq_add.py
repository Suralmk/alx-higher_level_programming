#!/usr/bin/python3


def uniq_add(my_list=[]):
    """
    A function that adds all the unique
    integers in a list
    """
    new = []
    total_sum = 0
    for num in my_list:
        if num not in new:
            total_sum += num
            new.append(num)
    return total_sum
