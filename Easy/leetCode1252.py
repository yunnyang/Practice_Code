# 1252. Cells with Odd Values in a Matrix

class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:

        matrix = [[0 for col in range(m)] for row in range(n)]
        oddNum = 0
        for r, c in indices:
            for i in range(m):
                matrix[r][i] += 1

            for j in range(n):
                matrix[j][c] += 1

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] % 2 == 1:
                    oddNum += 1

        return oddNum