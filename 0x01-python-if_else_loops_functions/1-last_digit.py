#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number < 0):
    value = ((number * -1) % 10) * -1
else:
    value = number % 10

if (value > 5):
    print(f"Last digit of {number:d} is {value:d}", end=' ')
    print(f"and is greater than 5")
elif (value == 0):
    print(f"Last digit of {number:d} is {value:d}", end=' ')
    print(f"and is 0")
else:
    print(f"Last digit of {number:d} is {value:d}", end=' ')
    print(f"and is less than 6 and not 0")
