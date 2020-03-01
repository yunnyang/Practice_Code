# 274. H-Index

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        H = 0
        indexs = []
        if len(citations) == 1:
            if citations[0] != 0:
                return 1
            else:
                return 0

        for i in range(len(citations)):
            index = self.getCitationNums(i + 1, citations)
            if index >= i + 1:
                if H < i + 1:
                    H = i + 1

        return H

    def getCitationNums(self, n, citations):
        count = 0

        for c in citations:
            if c >= n and c != 0:
                count += 1

        if count > max(citations):
            return max(citations)
        return count