#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newmatrix = []
    for i in matrix:
        newmatrix.append(list(map((lambda x: x * x), i)))
    return newmatrix
print (square_matrix_simple([[1,2,3], [4,5,5]]))
