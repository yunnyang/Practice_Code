# 279. Perfect Squares

class Solution:
    def numSquares(self, n: int) -> int:
        stack = collections.deque()
        result = 10000
        visited = set()

        stack.append((n, 0))

        while stack:
            target, time = stack.popleft()

            if target == 0:
                result = min(result, time)

            sqrtN = int(math.sqrt(target))

            for i in range(0, sqrtN + 1):
                if target - i * i not in visited:
                    visited.add(target - i * i)
                    stack.append((target - i * i, time + 1))

        return result
