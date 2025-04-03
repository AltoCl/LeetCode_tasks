# You are given a 0-indexed integer array nums.
#
# Return the maximum value over all triplets of indices (i, j, k) such that i < j < k. If all such triplets have a negative value, return 0.
#
# The value of a triplet of indices (i, j, k) is equal to (nums[i] - nums[j]) * nums[k].


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        L = [0] * n
        R = [0] * n
        for i in range(n - 1):
            L[i + 1] = max(L[i], nums[i])
            R[n - 2 - i] = max(R[n - i - 1], nums[n - i - 1])
        return max(0, max((L[i] - nums[i]) * R[i] for i in range(1, n - 1)))
