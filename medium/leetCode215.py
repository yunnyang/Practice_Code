# 215. Kth Largest Element in an Array


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        if len(nums) == 0:
            return -1

        for i in range(k - 1):
            nums.remove(max(nums))

        return max(nums)