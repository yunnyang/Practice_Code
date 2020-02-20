# 258. Add Digits

#자릿수근 공식을 이용해서 재귀나 반복문 없이 해결

class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0

        else:
            return 1 + (num - 1) % (10 - 1)