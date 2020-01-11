# 556. Next Greater Element III

# Use itertools ti make permutation
import itertools


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nStr = str(n)
        nList = list()

        for i in range(0, len(nStr)):
            nList.append(nStr[i])

        results = list(map(''.join, itertools.permutations(list(nList))))

        results = set(results)
        results = list(results)
        results.sort()
        if len(results) == 1:
            return -1

        for result in results:
            if int(result) > n:
                if -2147483648 < int(result) and int(result) < 2147483647:
                    return int(result)
                else:
                    return -1

        return -1