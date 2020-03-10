# 343. Integer Break

class Solution:
    ib = collections.defaultdict(int)

    def integerBreak(self, n: int) -> int:
        maxVal = -1

        if n <= 3:
            self.ib[n] = n
            return n - 1

        else:
            for i in range(1, int(n / 2) + 1):
                if n - i in self.ib.keys():
                    target = max(n - i, self.ib[n - i])
                    maxVal = max(maxVal, i * target)
                else:
                    self.ib[n - i] = self.integerBreak(n - i)
                    target = max(n - i, self.ib[n - i])
                    maxVal = max(maxVal, i * target)

        return maxVal