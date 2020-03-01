# 454. 4Sum II

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        length = len(A)
        if length == 0:
            return 0

        Sum1 = collections.defaultdict(int)
        Sum2 = collections.defaultdict(int)
        res = 0

        for i in range(length):
            for j in range(length):
                Sum1[A[i] + B[j]] += 1
                Sum2[C[i] + D[j]] += 1

        for s in Sum1.keys():
            if -s in Sum2.keys():
                res += Sum1[s] * Sum2[-s]

        return res