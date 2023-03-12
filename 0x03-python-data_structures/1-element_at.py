#!/usr/bin/python3
def element_at(my_list, idx):
    length = len(my_list)
    if idx < 0 or > length:
        return None
    element = my_list[idx]
    return element
