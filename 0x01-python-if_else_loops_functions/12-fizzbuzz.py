#!/usr/bin/python3

def fizzbuzz():

    for ss in range(1, 101):
        if ((ss % 3 == 0) and (ss % 5 == 0)):
            print('FizzBuzz', end=' ')
        elif (ss % 3 == 0):
            print('Fizz', end=' ')
        elif (ss % 5 == 0):
            print('Buzz', end=' ')
        else:
            print('{:d} '.format(ss), end='')
