#!/usr/bin/python3
# function that prints a string in uppercase


def uppercase(str):
    for letter in str:
        if ord(letter) >= 97 and ord(letter) <= 122:
            letter = chr(ord(letter) - 32)
        print('{}'.format(letter), end='')
    print('')
