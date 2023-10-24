#!/usr/bin/python3

for nu in range(0, 9):
    um = nu + 1

    while um <= 9:
        print("{:d}{:d}".format(nu, um), end='')
        print(end='\n' if nu == 8 else ", ")
        um += 1
