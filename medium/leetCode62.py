# 62. Unique Paths

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        if m == 1 or n == 1:
            return 1

        else:
            return int(self.factorial(m + n - 2) / (self.factorial(m - 1) * self.factorial(n - 1)))

    def factorial(self, num: int) -> int:
        if num == 1:
            return 1
        else:
            return num * self.factorial(num - 1)