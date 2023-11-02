#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num = len(sys.argv[1:])
    if (num == 0):
        print("{} arguments.".format(num))
    elif (num == 1):
        print("{} argument:".format(num))
        print("{}: {}".format(num, sys.argv[num]))
    else:
        print("{} arguments:".format(num))
        for r in range(num):
            print("{}: {}".format(r + 1, sys.argv[r + 1]))
