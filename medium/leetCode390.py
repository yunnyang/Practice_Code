#390. Elimination Game

class Solution:
    def lastRemaining(self, n: int) -> int:
        flag = 1  # odd

        odd = []
        even = []

        for num in range(1, n + 1):
            if flag == 1:
                odd.append(num)
            elif flag == -1:
                even.append(num)

            flag = flag * -1

        left = []

        if len(even) == 1:
            return even.pop()

        flag = 1  # init

        while True:

            if len(odd) == 1 or len(even) == 1:
                if len(odd) == 1:
                    return odd.pop()

                if len(even) == 1:
                    return even.pop()

            if flag == 1:
                nums = even
                odd = [i for i in nums if nums.index(i) % 2 == 0]

                if len(odd) > len(nums) / 2:
                    left = list(set(nums) - set(odd))
                    left.sort()
                    odd = left


            elif flag == -1:
                nums = odd
                even = [i for i in nums if nums.index(i) % 2 == 1]

                if len(even) > len(nums) / 2:
                    left = list(set(nums) - set(even))
                    left.sort()
                    even = left

            flag = flag * -1