#!/usr/bin/python3
for _ in range(1, 100):
    if _%3==0:
        print("Fizz", end=" ")
    elif _%5==0:
        print("Buzz", end=" ");
    elif _%3==0 and _%5==0:
        print("FizzBuzz", end=" ")
    else:
        print("{:d}".format(_), end=" ")
