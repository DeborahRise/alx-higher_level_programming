#!/usr/bin/python3
for r in range(97, 123):
    if (r == 101 or r == 113):
        continue
    print("{}".format(chr(r)), end='')
