# An array is considered special if every pair of its adjacent elements contains two numbers with different parity.
#
# You are given an array of integers nums. Return true if nums is a special array, otherwise, return false.

class Solution:
    def isArraySpecial(self, nums: list[int]) -> bool:
        for i in range(len(nums) - 1):
            if nums[i] % 2 == nums[i + 1] % 2:
                return False
        return True