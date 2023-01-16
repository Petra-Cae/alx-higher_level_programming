#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # computes the square value of all integers of a matrix
    sqr_matrix = [[x ** 2 for x in row] for row in matrix]
    return sqr_matrix
