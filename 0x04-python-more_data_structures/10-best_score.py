#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_value = 0
    for i in a_dictionary.values():
        if i > max_value:
            max_value = i
    return max_value
