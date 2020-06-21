# 675. Cut Off Trees for Golf Event
# Hard
#
# You are asked to cut off trees in a forest for a golf event. The forest is represented as a non-negative 2D map, in this map:
# 
# 0 represents the obstacle can't be reached.
# 1 represents the ground can be walked through.
# The place with number bigger than 1 represents a tree can be walked through, and this positive number represents the tree's height.
# In one step you can walk in any of the four directions top, bottom, left and right also when standing in a point which is a tree you can decide whether or not to cut off the tree.
#
# You are asked to cut off all the trees in this forest in the order of tree's height - always cut off the tree with lowest height first. And after cutting, the original place has the tree will become a grass (value 1).
#
# You will start from the point (0, 0) and you should output the minimum steps you need to walk to cut off all the trees. If you can't cut off all the trees, output -1 in that situation.
#
# You are guaranteed that no two trees have the same height and there is at least one tree needs to be cut off.

import collections


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        def stepHelper(befo, aftr):
            queue = collections.deque()
            visited = set()

            Dx = [-1, 0, 1, 0]
            Dy = [0, 1, 0, -1]

            ansLoca = (0, 0)
            minStep = 100000
            queue.append((befo, 0))
            visited.add(befo)

            while queue:
                loca, step = queue.popleft()

                x = loca[0]
                y = loca[1]

                if forest[x][y] == aftr:
                    ansLoca = (x, y)
                    minStep = min(minStep, step)
                    return ansLoca, minStep

                for dx, dy in zip(Dx, Dy):
                    if (x + dx >= 0 and x + dx < len(forest)) and (y + dy >= 0 and y + dy < len(forest[0])):
                        if forest[x + dx][y + dy] != 0 and (x + dx, y + dy) not in visited:
                            nextStep = (x + dx, y + dy)
                            queue.append((nextStep, step + 1))
                            visited.add(nextStep)

            if minStep == 100000:
                return ansLoca, -1
            else:
                return ansLoca, minStep

        ans = 0
        stforest = []

        for frt in forest:
            stforest.extend(frt)

        stforest.sort()
        stforest = [x for x in stforest if x > 1]

        aftr, ans = stepHelper((0, 0), stforest[0])

        if ans == -1:
            return -1

        for i in range(0, len(stforest) - 1):
            aftr, temp = stepHelper(aftr, stforest[i + 1])

            if temp == -1:
                return -1
            else:
                ans += temp

        return ans


