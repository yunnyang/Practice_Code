# 191. Number of 1 Bits

class Solution:
    def hammingWeight(self, n: int) -> int:
        i = 0
        while n != 0:
            n &= (n - 1)
            i += 1

        return i