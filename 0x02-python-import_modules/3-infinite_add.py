#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    ag = sys.argv[1:]
    num = len(ag)
    result = 0
    for r in range(num):
        result = result + int(ag[r])
    print("{}".format(result))
