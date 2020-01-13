# 11. Container With Most Water
#
# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
#
# Note: You may not slant the container and n is at least 2.


class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxWater = 0

        start = 0
        end = len(height) - 1

        while start < end:
            maxWater = max(maxWater, (end - start) * min(height[start], height[end]))

            if start + 1 < len(height) and height[start] <= height[end]:
                start = start + 1
            else:
                end = end - 1

        return maxWater

