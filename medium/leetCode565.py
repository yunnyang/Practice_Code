# 565. Array Nesting

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        S = []
        A = nums[:]
        visited = collections.defaultdict()

        result = 0
        if len(A) == 0:
            return 0

        for i in range(len(A)):
            S = []

            if A[i] not in visited:
                S.append(A[i])

                t = 1
                while True:

                    target = A[S[t - 1]]

                    if target in S:
                        break

                    S.append(target)
                    visited[target] = -1
                    t += 1

                visited[A[i]] = len(S)

                if result <= len(S):
                    result = len(S)

        return result
