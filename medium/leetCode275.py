# 275. H-Index II


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if len(citations) == 0:
            return 0

        for i in range(len(citations), -1, -1):
            if citations[-i] >= i:
                return i
        return 0