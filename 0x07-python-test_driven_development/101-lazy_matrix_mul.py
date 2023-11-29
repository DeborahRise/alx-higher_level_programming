#!/usr/bin/python3
"""
multiplication of 2 matrices using numpy lib

"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Returns:
        a multiplied matrix m_a and m_b
    Args:
        m_a: first matrix
        m_a: second
    """

    return (np.matmul(m_a, m_b))
