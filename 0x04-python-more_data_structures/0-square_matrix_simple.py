#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = [[col**2 for col in row] for row in matrix]
    return new_list
