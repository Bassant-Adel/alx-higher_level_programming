#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    nlist = []
    for a in range(list_length):

        zz = 0
        try:
            zz = my_list_1[a] / my_list_2[a]

        except TypeError:
            print("wrong type")

        except ZeroDivisionError:
            print("division by 0")

        except IndexError:
            print("out of range")

        finally:
            nlist.append(zz)
    return nlist
