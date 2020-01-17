# 34. Find First and Last Position of Element in Sorted Array

import bisect

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if len(nums) == 0:
            return [-1, -1]

        l = bisect.bisect_left(nums, target)
        r = bisect.bisect_right(nums, target)
        if l == r:
            if nums[0] == target:
                return [1, len(nums) - 1]
            else:
                return [-1, -1]
        else:
            if nums[l] != target:
                l = -1

            if nums[r - 1] != target:
                r = 0
            return [l, r - 1]
