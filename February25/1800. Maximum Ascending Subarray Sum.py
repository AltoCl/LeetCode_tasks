# Given an array of positive integers nums, return the maximum possible sum of an ascending subarray in nums.
#
# A subarray is defined as a contiguous sequence of numbers in an array.
#
# A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i where l <= i < r, numsi  < numsi+1. Note that a subarray of size 1 is ascending.


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxSum=Sum=nums[0]
        for x, y in pairwise(nums):
            Sum=y if y<=x else Sum+y
            maxSum=max(maxSum, Sum)
        return maxSum