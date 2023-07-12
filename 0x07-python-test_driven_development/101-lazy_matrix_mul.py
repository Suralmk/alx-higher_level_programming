#!/usr/bin/python3
"""matrix multiplication using numpy"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """return the result of multiplication of two matrix.
    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    """

    return (np.matmul(m_a, m_b))
