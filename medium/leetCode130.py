# 130. Surrounded Regions

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        start = []

        Dx = [-1, 0, 1, 0]
        Dy = [0, 1, 0, -1]

        for i in range(1, len(board) - 1):
            for j in range(1, len(board[0]) - 1):
                if board[i][j] == 'O':
                    isBoarder = False
                    start = [i, j]
                    queue = collections.deque()
                    queue.append(start)
                    visited = set()
                    area = set()
                    area.add((i, j))

                    while queue:
                        target = queue.popleft()
                        x = target[0]
                        y = target[1]
                        visited.add((x, y))
                        if isBoarder == True:
                            break

                        for dx, dy in zip(Dx, Dy):
                            if x + dx >= 0 and x + dx < len(board) and y + dy >= 0 and y + dy < len(board[0]):
                                if board[x + dx][y + dy] == 'O':
                                    if (x + dx, y + dy) not in visited:
                                        queue.append([x + dx, y + dy])
                                        area.add((x + dx, y + dy))
                                    if x + dx == 0 or x + dx == len(board) - 1 or y + dy == 0 or y + dy == len(
                                            board[0]) - 1:
                                        isBoarder = True
                                        break

                    if isBoarder == False:
                        for a in area:
                            x = a[0]
                            y = a[1]

                            board[x][y] = 'X'
