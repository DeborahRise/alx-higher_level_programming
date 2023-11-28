#!/usr/bin/python3
"""
multiplication of matrix using numpy lib

"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return: a nex matrix with the product of m_a and m_b
    """
    return (np.matmul(m_a, m_b))
