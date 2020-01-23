# 78. Subsets

import itertools


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        for i in range(len(nums) + 1):
            element = list(itertools.combinations(nums, i))
            result.extend(element)

        return result
