#390. Elimination Game

class Solution:
    def lastRemaining(self, n: int) -> int:
        L2R = 1
        head = 1
        remaining = n
        steps = 1

        while remaining > 1:
            # if L2R == 1 or remaining & 1:
            if L2R == 1 or remaining % 2 == 1:
                head += steps

            remaining //= 2
            steps *= 2
            # L2R ^= 1
            L2R = 1 - L2R

        return head