# 480. Sliding Window Median
import bisect

class Solution:
    def medianSlidingWindow(self, nums, k: int) :
        window = sorted(nums[:k])
        medians = []

        for a, b in zip(nums, nums[k:] + [0]):
            medians.append((window[int(k / 2)] + window[~int(k / 2)]) / 2.)
            window.remove(a)
            bisect.insort(window, b)

        return medians

# Refer to
# https://leetcode.com/problems/sliding-window-median/discuss/96355/Easy-Python-O(nk)