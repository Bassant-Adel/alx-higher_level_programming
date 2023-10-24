#!/usr/bin/python3

for ss in range(122, 96, -1):

    if ss % 2 != 0:
        ss = ss - 32
    print('{:s}'.format(chr(ss)), end='')
