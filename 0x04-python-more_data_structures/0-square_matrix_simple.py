#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    function that computes square of a matrix
    """
    sq_matrix = []
    for column in matrix:
        result = list(map(lambda x: x**2, column))
        sq_matrix.append(result)
    return sq_matrix
