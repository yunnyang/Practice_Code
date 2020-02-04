# 486. Predict the Winner


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        dp = nums[:]
        for i in range(1, len(nums)):
            for j in range(len(nums) - i):
                dp[j] = max(nums[j] - dp[j + 1], nums[j + i] - dp[j])

        return dp[0] >= 0

