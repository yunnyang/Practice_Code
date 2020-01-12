# 240. Search a 2D Matrix ||

# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
#
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
# Example:
#
# Consider the following matrix:
#
# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]

# Given target = 5, return true.
#
# Given target = 20, return false.

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if len(matrix) == 0:
            return False

        if len(matrix[0]) == 0:
            return False

        if len(matrix[0]) == 1:
            for m in range(0, len(matrix)):
                if matrix[m][0] == target:
                    return True

        for n in range(0, len(matrix[0])):

            if matrix[0][n] == target:
                return True

            if matrix[0][n] > target:
                for m in range(0, len(matrix)):
                    if matrix[m][n - 1] == target:
                        return True

            for m in range(0, len(matrix)):
                if matrix[m][n] == target:
                    return True
        return False
