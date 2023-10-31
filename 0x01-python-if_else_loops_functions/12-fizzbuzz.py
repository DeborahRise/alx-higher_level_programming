#!/usr/bin/python3
def fizzbuzz():
    for r in range(1, 101):
        if (r % 3 == 0 and r % 5 == 0):
            print("FizzBuzz ", end='')
        elif (r % 5 == 0):
            print("Buzz ", end='')
        elif (r % 3 == 0):
            print("Fizz ", end='')
        else:
            print("{} ".format(r), end='')
