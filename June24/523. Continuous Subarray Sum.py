# Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.
#
# A good subarray is a subarray where:
#
# its length is at least two, and
# the sum of the elements of the subarray is a multiple of k.
# Note that:
#
# A subarray is a contiguous part of the array.
# An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mod_k_prefixes = set()
        prev_prefix_sum = 0  # For empty subarray
        nums[0] %= k
        for prefix_sum in accumulate(nums, lambda a, b: (a + b) % k):
            if prefix_sum in mod_k_prefixes:
                return True
            else:
                mod_k_prefixes.add(prev_prefix_sum)  # Add prefix sum to the set with 1 step delay
                prev_prefix_sum = prefix_sum

        return False