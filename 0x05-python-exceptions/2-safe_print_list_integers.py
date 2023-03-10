#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    # prints the first x elements of a list that are integers
    count = 0
    for el in range(x):
        try:
            print("{:d}".format(my_list[el]), end="")
            count += 1
        except (TypeError, ValueError):
            continue
    print()
    return (count)
