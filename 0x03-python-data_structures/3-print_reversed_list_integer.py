#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    # prints all integers of a list in reverse order
    if my_list:
        for i in range(len(my_list)):
            my_list.reverse()
            print('{:d}'.format(my_list[i]))
    else:
        pass
