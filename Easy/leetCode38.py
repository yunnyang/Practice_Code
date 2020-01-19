# 38. Count and Say
#
# The count-and-say sequence is the sequence of integers with the first five terms as following:
#
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
#
# Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence. You can do so recursively, in other words from the previous member read off the digits, counting the number of digits in groups of the same digit.

class Solution:
    def countAndSay(self, n: int) -> str:
        seqDict = dict()
        seqDict[1] = '1'
        seqDict[2] = '11'
        seqDict[3] = '21'
        if n == 1:
            return '1'

        else:
            if n - 1 in seqDict:
                seq = seqDict[n - 1]
            else:
                seq = self.countAndSay(n - 1)
                seqDict[n - 1] = seq

            changeSeq = ""
            count = 1
            if seq == '1':
                return '11'
            elif seq == '11':
                return '21'

            for i in range(len(seq) - 1, -1, -1):
                if i == 0:
                    changeSeq = str(count) + seq[i] + changeSeq
                    seqDict[n] = changeSeq

                elif seq[i] == seq[i - 1]:
                    count = count + 1

                else:
                    changeSeq = str(count) + seq[i] + changeSeq
                    count = 1
                    seqDict[n] = changeSeq

            return changeSeq