# Given an integer array nums, return the number of subarrays filled with 0.
#
# A subarray is a contiguous non-empty sequence of elements within an array.

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        return (Len := 0) or sum(Len := Len + 1 if x == 0 else 0 for x in nums)
