# 239. Sliding Window Maximum

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = []
        result = []

        if len(nums) == 0:
            return []

        for i in range(len(nums) - k + 1):
            window = nums[i:i + k]
            result.append(max(window))

        return result
