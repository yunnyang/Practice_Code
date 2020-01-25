# 73. Set Matrix Zeroes

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroPoint = []
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                if matrix[i][j] == 0:
                    zeroPoint.append([i, j])

        for x, y in zeroPoint:
            for i in range(len(matrix[x])):
                matrix[x][i] = 0
            for j in range(len(matrix)):
                matrix[j][y] = 0



