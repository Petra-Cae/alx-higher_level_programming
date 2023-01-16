#!/usr/bin/python3
def uniq_add(my_list=[]):
    # adds all unique integers in a list (once for each integer)
    newList = set(my_list)
    result = 0
    for number in newList:
        result += number
    return result
