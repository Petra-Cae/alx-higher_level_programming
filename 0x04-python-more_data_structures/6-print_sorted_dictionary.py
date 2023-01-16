#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # prints a dictionary by ordered keys
    for a_string in sorted(a_dictionary):
        print("{:s}: {}".format(a_string, a_dictionary[a_string]))
