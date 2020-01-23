#66. Plus One

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] = digits[-1] + 1

        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 10:
                if i >= 1:
                    digits[i - 1] = digits[i - 1] + 1
                    digits[i] = 0

                else:
                    digits[i] = 0
                    digits.insert(0, 1)

        return digits