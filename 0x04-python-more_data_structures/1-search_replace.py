#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Replaces occurences of an element in a new list
    list_copy = []
    for number in range(len(my_list)):
        if my_list[number] == search:
            list_copy.append(replace)
        else:
            list_copy.append(my_list[number])
    return list_copy
