# 121. Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0 for _ in range(len(prices))]

        if len(prices) <= 1:
            return 0

        dp[0] = 0

        for i in range(1, len(prices)):
            dp[i] = max(dp[i - 1], prices[i] - min(prices[:i]))

        return max(dp)