#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # Replaces an element in a list at a specific index
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list

    copy = [el for el in my_list]
    copy[idx] = element
    return copy
