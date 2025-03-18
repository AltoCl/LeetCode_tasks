# You are given an array nums consisting of positive integers.
#
# We call a subarray of nums nice if the bitwise AND of every pair of elements that are in different positions in the subarray is equal to 0.
#
# Return the length of the longest nice subarray.
#
# A subarray is a contiguous part of an array.
#
# Note that subarrays of length 1 are always considered nice.

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n, ans, B, l=len(nums), 0, 0, 0
        for r, x in enumerate(nums):
            while l<r and (B& x)!=0:
                B^=nums[l]
                l+=1
            B|=x
            ans=max(ans, r-l+1)
        return ans