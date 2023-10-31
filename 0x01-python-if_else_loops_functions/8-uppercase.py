#!/usr/bin/python3
def uppercase(str):
    for s in str:
        if (ord(s) >= 97 and ord(s) <= 122):
            value = chr(ord(s) - 32)
        else:
            value = s
        print("{}".format(value), end='')
    else:
        print()
