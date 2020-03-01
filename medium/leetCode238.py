# 238. Product of Array Except Self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        product = 1
        zeroFlag = False

        if 0 in set(nums) and len(set(nums)) == 1:
            return [0 for i in range(len(nums))]

        for num in nums:
            if num != 0:
                product = product * num
            else:
                zeroFlag = True

        if nums.count(0) > 1:
            product = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                if zeroFlag == False:
                    output.append(int(product / nums[i]))
                else:
                    output.append(0)
            else:
                output.append(product)

        return output