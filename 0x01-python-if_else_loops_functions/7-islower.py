#!/usr/bin/python3

"""checks if the charachter is lowwercase or uppercase"""
def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
