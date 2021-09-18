#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    i = -1 * int(str(number)[-1])
else:
    i = number % 10
if (i > 5):
    tmp = "is greater than 5"
elif (i < 6 and i != 0):
    tmp = "is less than 6 and not 0"
elif (i == 0):
    tmp = "is 0"
print("Last digit of {:n} is {} and {}".format(number, i, tmp))
