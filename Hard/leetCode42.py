# 42. Trapping Rain Water

import bisect


class Solution:
    def trap(self, height: List[int]) -> int:

        if len(height) == 0:
            return 0

        MaxNum = max(height)
        heights = height
        index = []
        water = []

        for i in range(len(height)):
            if height[i] == MaxNum:
                index.append(i)

        if index[0] != 0:
            index.insert(0, 0)

        if index[-1] != len(height) - 1:
            index.append(len(height) - 1)

        for i in range(len(index) - 1):
            heights = height[index[i]:index[i + 1] + 1]
            partWater = self.trapHelper(heights)
            water.append(partWater)

        return sum(water)

    def trapHelper(self, height: List[int]) -> int:
        concave = 0
        bowl = []
        water = 0
        Max = 0
        heights = []

        if len(height) <= 2:
            return 0

        AllMax = max(height)

        if len(height) == 3:
            if height.index(min(height)) != 1:
                return 0
            else:
                height.remove(max(height))
                return abs(height[0] - height[1])

        if height[0] == AllMax:
            height.reverse()

        for i in range(len(height) - 1):

            if height[i] > Max:
                Max = height[i]
                if Max == AllMax and i != 0:
                    Max = 0  # reset

            concave = height[i] - height[i + 1]
            if concave >= 0:
                if Max - height[i] > 0:
                    bowl.append(Max - height[i])

            if concave < 0 and i != 0:
                if Max - height[i] > 0:
                    bowl.append(Max - height[i])
                if height[i + 1] >= Max:
                    water = water + sum(bowl)
                    bowl = []

        return water