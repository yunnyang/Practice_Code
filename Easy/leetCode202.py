# 202. Happy Number

class Solution:
    def isHappy(self, n: int) -> bool:

        letters = str(n)
        cycle = set()

        i = 0
        while i < 100:
            num = 0
            for letter in letters:
                num += int(letter) * int(letter)

            if num == 1:
                return True

            if num in cycle:
                return False
            else:
                cycle.add(num)

            i += 1
            letters = str(num)

        return False
