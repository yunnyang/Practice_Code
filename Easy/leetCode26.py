# 26. Remove Duplicates from Sorted Array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        length = len(nums) - 1

        while i < length:
            if nums[i] == nums[i + 1]:
                nums.pop(i)
                length = length - 1

            else:
                i = i + 1

