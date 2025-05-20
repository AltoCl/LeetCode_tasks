# You are given an integer array nums of length n and a 2D array queries, where queries[i] = [li, ri].
#
# For each queries[i]:
#
# Select a subset of indices within the range [li, ri] in nums.
# Decrement the values at the selected indices by 1.
# A Zero Array is an array where all elements are equal to 0.
#
# Return true if it is possible to transform nums into a Zero Array after processing all the queries sequentially, otherwise return false.


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)
        for li, ri in queries:
            diff[li] -= 1
            if ri + 1 < n:
                diff[ri + 1] += 1
        sum_val = 0
        for i in range(n):
            sum_val += diff[i]
            if nums[i] > -sum_val:
                return False
        return True