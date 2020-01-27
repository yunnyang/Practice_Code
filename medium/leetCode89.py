# 89. Gray Code
#
# The gray code is a binary numeral system where two successive values differ in only one bit.
#
# Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.
#
# Example 1:
#
# Input: 2
# Output: [0,1,3,2]
# Explanation:
# 00 - 0
# 01 - 1
# 11 - 3
# 10 - 2
#
# For a given n, a gray code sequence may not be uniquely defined.
# For example, [0,2,3,1] is also a valid gray code sequence.
#
# 00 - 0
# 10 - 2
# 11 - 3
# 01 - 1


class Solution:
    def grayCode(self, n: int) -> List[int]:
        grayCodeSeq = []

        for i in range(int(math.pow(2, n))):
            grayCodeSeq.append(self.binaryToGray(i))

        return grayCodeSeq

    def binaryToGray(self, num):
        return num ^ (num >> 1)

    def grayToBinary32(self, num):
        num = num ^ (num >> 16);
        num = num ^ (num >> 8);
        num = num ^ (num >> 4);
        num = num ^ (num >> 2);
        num = num ^ (num >> 1);
        return num;