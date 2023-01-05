#!/usr/bin/python3
# function that prints a string in uppercase


def uppercase(str):
    for letter in str:
        if ord(letter) > 96 and ord(letter) < 123:
            letter = chr(ord(letter) - 32)
        print('{}'.format(letter), end='')
    print('')
