# 347. Top K Frequent Elements

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countDict = collections.defaultdict(int)

        if k == 0 or len(nums) == 0:
            return []

        elif k > len(nums):
            return []

        for num in nums:
            countDict[num] += 1

        countList = sorted(countDict.items(), key=lambda x: x[1], reverse=True)

        i = 0

        answer = []

        while i < k:
            answer.append(countList.pop(0)[0])
            i += 1

            if len(countList) == 0:
                break

        return answer
