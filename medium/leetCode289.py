# 289. Game of Life

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        Live = []
        Die = []

        for m in range(0, len(board)):
            for n in range(0, len(board[0])):
                if self.LiveOrDie(board, [m, n]) == True:
                    Live.append([m, n])

                else:
                    Die.append([m, n])

        for x, y in Live:
            board[x][y] = 1

        for x, y in Die:
            board[x][y] = 0

    def LiveOrDie(self, board, location):
        x = location[0]
        y = location[1]

        die = 0
        live = 0

        Live = []
        Die = []

        for i in range(-1, 2):
            for j in range(-1, 2):
                if i != 0 or j != 0:
                    if x + i >= 0 and y + j >= 0 and x + i < len(board) and y + j < len(board[0]):
                        if board[x + i][y + j] == 0:
                            die += 1
                        elif board[x + i][y + j] == 1:
                            live += 1

        if board[x][y] == 1:
            if live < 2:
                return False

            elif live == 2 or live == 3:
                return True

            elif live > 3:
                return False

            else:
                return True

        else:
            if live == 3:
                return True

            else:
                return False