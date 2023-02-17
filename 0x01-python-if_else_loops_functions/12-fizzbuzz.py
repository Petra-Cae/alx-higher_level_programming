#!/usr/bin/python3
def fizzbuzz():
    """
    Prints numbers from 1 to 100 seperated by a space;
    for multiples of 3, Fizz is printed,
    for multiples of 5, Buzz is printed,
    for multiples of both 3 and 5, FizzBuzz is printed
    """

    for number in range(1, 101):
        if number % 3 == 0:
            print("Fizz ", end="")
        elif number % 5 == 0:
            print("Buzz ", end="")
        elif number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
        else:
            print("{} ".format(number), end="")
