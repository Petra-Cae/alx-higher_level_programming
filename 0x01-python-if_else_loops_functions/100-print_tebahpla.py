#!/usr/bin/python3
"""
    Prints the ASCII alphabet in reverse order
    alternating lowercase and uppercase, without a new line
"""
alphabet = ""
for alphab_count in range(122, 96, -1):
    if alphab_count % 2 == 0:
        alphabet += chr(alphab_count)
    else:
        alphabet += chr(alphab_count - 32)
print("{}".format(alphabet), end="")
