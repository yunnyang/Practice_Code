322. Coin Change


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        queue = collections.deque()

        if len(coins) == 0:
            return -1

        if amount == 0:
            return 0

        coinSum = 0
        coinCount = 0

        queue.append((amount, 0))
        visited = set()
        while queue:
            target = queue.pop()

            coinSum = target[0]
            coinCount = target[1]

            for coin in coins:

                if coinSum - coin == 0:
                    return coinCount + 1

                elif coinSum - coin < 0:
                    continue

                elif coinSum - coin not in visited:
                    visited.add(coinSum - coin)
                    queue.appendleft((coinSum - coin, coinCount + 1))

        return -1