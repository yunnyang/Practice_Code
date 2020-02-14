# 56. Merge Intervals

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []
        i = 0
        while intervals:
            after = intervals.pop(0)

            if len(result) == 0:
                result.append(after)
            else:
                before = result[-1]

                if before[1] >= after[0]:
                    before[1] = max(after[1], before[1])
                else:
                    result.append(after)

        return result