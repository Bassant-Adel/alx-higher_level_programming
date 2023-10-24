#!/usr/bin/python3
""" KEYS """


def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    rno = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    rw = roman_string
    for b in range(len(rw)):
        if b < len(rw) - 1 and rno[rw[b]] < rno[rw[b + 1]]:
            sum -= rno[rw[b]]
        else:
            sum += rno[rw[b]]
    return sum
