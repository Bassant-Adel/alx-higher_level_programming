#!/usr/bin/python3

def remove_char_at(str, n):
    dd = ''

    for ss in range(len(str)):
        if ss != n:
            dd += str[ss]
    return (dd)
