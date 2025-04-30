# Given an array nums of integers, return how many of them contain an even number of digits.

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(int(floor(log10(x)) + 1) % 2 == 0 for x in nums)
