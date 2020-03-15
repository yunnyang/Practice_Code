# 397. Integer Replacement

class Solution:
    def integerReplacement(self, n: int) -> int:
        queue = collections.deque()
        visited = set()

        if n == 0:
            return 0

        queue.append((n, 0))

        while queue:
            num, r = queue.popleft()

            if num == 1:
                return r

            if num % 2 == 0:
                if (int(num / 2), r + 1) not in visited:
                    visited.add((int(num / 2), r + 1))
                    queue.append((int(num / 2), r + 1))

            else:
                if (num - 1, r + 1) not in visited:
                    visited.add((num - 1, r + 1))
                    queue.append((num - 1, r + 1))

                if (num + 1, r + 1) not in visited:
                    visited.add((num + 1, r + 1))
                    queue.append((num + 1, r + 1))



