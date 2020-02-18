# 200. Number of Islands


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        stack = collections.deque()

        island = 0
        visited = set()

        Dx = [1, 0, -1, 0]
        Dy = [0, 1, 0, -1]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i, j) not in visited:
                    stack.append((i, j))

                    while stack:
                        target = stack.pop()
                        visited.add(target)

                        x = target[0]
                        y = target[1]

                        for dx, dy in zip(Dx, Dy):
                            if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]):
                                if grid[x + dx][y + dy] == '1' and (x + dx, y + dy) not in visited:
                                    stack.append((x + dx, y + dy))

                    island += 1

        return island



