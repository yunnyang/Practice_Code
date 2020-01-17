# 41. First Missing Positive

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 1

        Max = max(nums)

        if Max <= 0:
            return 1

        for i in range(1, Max + 1):
            if i not in nums:
                return i

        return Max + 1