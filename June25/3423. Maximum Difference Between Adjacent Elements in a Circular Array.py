# Given a circular array nums, find the maximum absolute difference between adjacent elements.
#
# Note: In a circular array, the first and last elements are adjacent.


class Solution:
    def maxAdjacentDistance(self, nums):
        n = len(nums)
        maxa = abs(nums[0] - nums[-1])
        for i in range(n - 1):
            maxa = max(maxa, abs(nums[i] - nums[i + 1]))
        return maxa