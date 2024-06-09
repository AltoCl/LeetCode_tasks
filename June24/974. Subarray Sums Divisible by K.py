# Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.
#
# A subarray is a contiguous part of an array.

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)

        for i in range(n):
            curr_sum = 0
            for j in range(i, n):
                curr_sum += nums[j]
                if curr_sum % k == 0:
                    count += 1

        return count