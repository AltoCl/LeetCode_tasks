# Given an integer array nums that does not contain any zeros,
# find the largest positive integer k such that -k also exists in the array.
#
# Return the positive integer k. If there is no such integer, return -1.

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        num_set = set(nums)

        max_positive = -1
        for num in nums:
            if -num in num_set:
                max_positive = max(max_positive, num)

        return max_positive if max_positive != -1 else -1