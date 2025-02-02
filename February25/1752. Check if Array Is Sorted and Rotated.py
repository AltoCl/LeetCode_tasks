# Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.
#
# There may be duplicates in the original array.
#
# Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.

class Solution:
    def check(self, nums: List[int]) -> bool:
        return (cntD:=sum(y<x for x, y in pairwise(nums)))==0 or (cntD==1 and nums[-1]<=nums[0])
