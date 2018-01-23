# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
# For example,

# Consider the following matrix:

# [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# Given target = 3, return true.


def search_matrix(matrix, target):
    """
    LC 74
    We know the matrix has a[i][j] > a[i][j - 1] sorted
    Also, a[i][0] > a[i - 1][-1] sequential.
    """
    for i in range(len(matrix)):
        if matrix[i][0] == target:
            return True
        elif matrix[i][0] > target and (i - 1) >= 0:  # if I am less than first, means if I exist I must be above, and above must be valid first
            for j in range(len(matrix[i - 1])):
                if matrix[i - 1][j] == target:
                    return True
        if i == (len(matrix) - 1) and target > matrix[i][0]:  # if I am in the last row
            for j in range(len(matrix[i])):
                if matrix[i][j] == target:
                    return True
    return False
