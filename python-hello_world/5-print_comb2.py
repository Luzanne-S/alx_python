#!/usr/bin/python3
for numbers in range(100):
    decimal_numbers = round(numbers)
    print("{:02d}".format(decimal_numbers), end=", " if decimal_numbers < 99 else "\n")
  