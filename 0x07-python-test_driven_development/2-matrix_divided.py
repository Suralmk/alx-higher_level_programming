#!/usr/bin/python3
"""Matrix devision function."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.
    Args:
        matrix (list): A matrix.
        div (int/float): The divisor.
    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.
    Returns:
        A the devision of the two martrixes.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(i, list) for i in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for i in matrix for num in i])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(i) == len(matrix[0]) for i in matrix):
        raise TypeError("Each i of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), i)) for i in matrix])
