# 228. Summary Ranges


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        answer = []
        flag = False

        if len(nums) == 0:
            return []

        if len(nums) == 1:
            return [str(nums[0])]

        elif len(nums) == 2:
            if nums[1] - nums[0] != 1:
                return [str(nums[0]), str(nums[1])]
            else:
                return [str(nums[0]) + "->" + str(nums[1])]

        start = 0
        end = 0
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] != 1:
                flag = True
                end = i
                if start == end:
                    subStr = str(nums[start])
                else:
                    subStr = str(nums[start]) + "->" + str(nums[end])
                answer.append(subStr)
                start = end + 1

        if flag == False:
            return [str(nums[0]) + "->" + str(nums[-1])]

        if len(nums[end + 1:]) != 0:
            if len(nums[end + 1:]) == 1:
                answer.append(str(nums[end + 1]))

            else:
                answer.append(str(nums[end + 1]) + "->" + str(nums[-1]))

        return answer
