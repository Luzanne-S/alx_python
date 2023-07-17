#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 5:
    print("Last digit of {} and is greater than 5 \n".format(number))
elif number == 0:
    print("Last digit of {} and is 0 \n".format(number))
else:
    print("Last digit of {} and is less than 6 and not 0 \n".format(number))