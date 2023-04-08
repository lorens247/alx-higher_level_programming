#!/usr/bin/python3
"""
This is the "2-matrix_divided" module.
The 2-matrix_divided module contains a function called matrix_divided(matrix, div),
which divides all elements in the matrix by div and returns a new matrix.
"""

def matrix_divided(matrix, div):
    """Divides all elements in the matrix by div"""
    # Check that matrix is a list of lists containing only integers or floats
    if type(matrix) is not list or not all(isinstance(l, list) and all(isinstance(i, (int, float)) for i in l) for l in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check that each row of matrix has the same length
    size = len(matrix[0])
    if not all(len(l) == size for l in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check that div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check that div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide each element of the matrix by div, rounded to 2 decimal places
    return [[round(i / div, 2) for i in l] for l in matrix]
