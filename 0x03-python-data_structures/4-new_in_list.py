#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list)
    if idx < 0 or idx >= length:
        return my_list
    new_list = [0] * length
    for i in range(0, length):
        new_list[i] = my_list[i]
    new_list[idx] = element
    return new_list
