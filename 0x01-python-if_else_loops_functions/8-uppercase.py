#!/usr/bin/python3

"""changes a sallcase senstense to uppercase"""
def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            i = chr(ord(i) - 32)
        print("{}".format(i), end='')
    print()
