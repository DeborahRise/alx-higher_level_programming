#!/usr/bin/python3
i = 0
while (i < 8):
    j = i + 1
    while (j < 10):
        print("{}{}, ".format(i, j), end='')
        j = j + 1
    i = i + 1
else:
    print("{}{}".format(i, i + 1))
