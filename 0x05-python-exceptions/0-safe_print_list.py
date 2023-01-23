#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    # prints x elements of a list
    count = 0
    for el in range(x):
        try:
            print("{}".format(my_list[el]), end="")
        except IndexError:
            break
        else:
            count += 1
    print()
    return (count)
