"""
Given a boolean matrix, update it so that if any cell is true, all the cells in the row and column are tru
"""
import numpy as np


class MATRIX_2D:
    def __init__(self, row: int, col: int, arr: list):
        self.row = row
        self.col = col
        self.arr = arr


def two_d_matrix():
    row = int(input("How many Rows?: "))
    col = int(input("How many Columns?: "))
    matrix = MATRIX_2D(row, col, [])
    matrix.row = row
    matrix.col = col
    matrix.arr = [[input(f"matrix[{i}][{j}]") for j in range(col)] for i in range(row)]
    return matrix


def z_matrix(matrix: two_d_matrix):
    true_list = []
    for i in range(matrix.row):
        for j in range(matrix.col):
            if matrix.arr[i][j] == 'true':
                true_list.append((i, j))   # List of matrix elements that are 'true'
    for x in true_list:
        line, column = x[0], x[1]
        i = 0
        for i in range(matrix.col): matrix.arr[line][i] = 'true'
        for i in range(matrix.row): matrix.arr[i][column] = 'true'
    return matrix.arr


matrix = two_d_matrix()
myarray = np.array(z_matrix(matrix))
#myarray = np.array(matrix.arr)
print(myarray)