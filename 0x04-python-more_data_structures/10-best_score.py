#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_value = 0
    for value in a_dictionary.values():
        if value > max_value:
            max_value = value
    for key, value in a_dictionary.items():
        if value == max_value:
            return key
