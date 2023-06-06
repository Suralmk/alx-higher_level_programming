#!/usr/bin/python3
i = ord('a')
while (i < ord('z')):
    if (i != ord('e') and i != ord('q')):
        print('{:c}'.format(i), end='')
    i = i + 1
