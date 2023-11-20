#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    value = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            value = value + 1
        except IndexError:
            break
    print("")
    return value
