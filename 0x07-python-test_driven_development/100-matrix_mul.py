#!/usr/bin/python3
"""Defines a matrix multiplication function."""


def matrix_mul(m_a, m_b):
    """Multiply two matrices.
    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    Raises:
        TypeError: If either m_a or m_b is not a list of lists of ints/floats.
        TypeError: If either m_a or m_b is empty.
        TypeError: If either m_a or m_b has different-sized rows.
        ValueError: If m_a and m_b cannot be multiplied.
    Returns:
        A new matrix representing the multiplication of m_a by m_b.
    """

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(i, list) for i in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(i, list) for i in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [j for i in m_a for j in i]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [j for i in m_b for j in i]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(i) == len(m_a[0]) for i in m_a):
        raise TypeError("each i of m_a must should be of the same size")
    if not all(len(i) == len(m_b[0]) for i in m_b):
        raise TypeError("each i of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    inverted_b = []
    for r in range(len(m_b[0])):
        new_i = []
        for c in range(len(m_b)):
            new_i.append(m_b[c][r])
        inverted_b.append(new_i)

    matrix = []
    for i in m_a:
        new_i = []
        for col in inverted_b:
            prod = 0
            for i in range(len(inverted_b[0])):
                prod += i[i] * col[i]
            new_i.append(prod)
        matrix.append(new_i)

    return matrix
