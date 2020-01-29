# 461. Hamming Distance

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        n = int(bin(x ^ y), 2)
        i = 0
        while n != 0:
            n &= (n - 1)
            i += 1

        return i