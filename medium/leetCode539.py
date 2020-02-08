# 593. Valid Square
#
# Given the coordinates of four points in 2D space, return whether the four points could construct a square.
#
# The coordinate (x,y) of a point is represented by an integer array with two integers.
#
# Example:
#
# Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
# Output: True

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        p = [p1, p2, p3, p4]

        f = sorted(p, key=lambda x: (-x[0], -x[1]))
        f1 = f[0]
        f2 = f[1]
        f3 = f[2]
        f4 = f[3]

        up = abs(f1[0] - f3[0])
        left = abs(f3[1] - f4[1])
        right = abs(f1[1] - f2[1])
        down = abs(f2[0] - f4[0])

        d1 = math.sqrt(math.pow(f1[0] - f4[0], 2) + math.pow(f1[1] - f4[1], 2))
        d2 = math.sqrt(math.pow(f2[0] - f3[0], 2) + math.pow(f2[1] - f3[1], 2))

        return (up == down) and (left == right) and (up == left) and d1 == d2 and up != 0