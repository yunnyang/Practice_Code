#54. Spiral Matrix

# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
#
# Example 1:
#
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        length = len(matrix)

        if length == 0:
            return []

        while length != 0:
            try:
                # step 1. Right

                result.extend(matrix[0])
                matrix.remove(matrix[0])

                # step 2. Down
                for i in range(len(matrix)):
                    result.append(matrix[i][len(matrix[i]) - 1])
                    matrix[i].pop(len(matrix[i]) - 1)

                # step 3. Left

                matrix[len(matrix) - 1].reverse()

                result.extend(matrix[len(matrix) - 1])
                matrix.pop(len(matrix) - 1)

                # step 4. Up

                for i in range(len(matrix) - 1, -1, -1):
                    result.append(matrix[i][0])
                    matrix[i].pop(0)
            except:
                break

        return result




