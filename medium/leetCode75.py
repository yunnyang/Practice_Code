# 75. Sort Colors
#
# Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.
#
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
#
# Note: You are not suppose to use the library's sort function for this problem.
#
# Example:
#
# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = 0  # 0
        white = 0  # 1

        for i in range(len(nums)):
            if nums[i] == 0:
                red += 1

            elif nums[i] == 1:
                white += 1

        for i in range(0, red):
            nums[i] = 0

        for i in range(red, red + white):
            nums[i] = 1

        for i in range(red + white, len(nums)):
            nums[i] = 2
