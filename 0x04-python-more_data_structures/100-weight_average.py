#!/usr/bin/python3
def weight_average(my_list=[]):
    # returns the weighted average of all integers in a tuple
    if not my_list:
        return 0
    average = 0
    div = 0
    for tup in my_list:
        average += tup[0] * tup[1]
        div += tup[1]
    return float(average / div)
