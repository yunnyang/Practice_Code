# 169. Majority Element

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numDict = collections.defaultdict(int)
        majority = -1
        for num in nums:
            oldValue = numDict[num]
            numDict[num] = oldValue + 1

            if numDict[majority] > int(len(nums) / 2):
                return majority

            if numDict[majority] <= numDict[num]:
                majority = num

        return majority