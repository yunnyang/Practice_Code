# 260. Single Number III
#
# Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.
#
# Example:
#
# Input:  [1,2,1,3,2,5]
# Output: [3,5]


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        exist = set()

        for num in nums:
            if num in exist:
                exist.remove(num)

            elif num not in exist:
                exist.add(num)

        return list(exist)
