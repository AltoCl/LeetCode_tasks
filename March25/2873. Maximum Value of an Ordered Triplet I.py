# You are given a 0-indexed integer array nums.
#
# Return the maximum value over all triplets of indices (i, j, k) such that i < j < k. If all such triplets have a negative value, return 0.
#
# The value of a triplet of indices (i, j, k) is equal to (nums[i] - nums[j]) * nums[k].

class Solution:
    def maximumTripletValue(self, nums):
        max_value = 0
        n = len(nums)

        # Iterate all possible triplets (i, j, k) where i < j < k
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    current_value = (nums[i] - nums[j]) * nums[k]
                    if current_value > max_value:
                        max_value = current_value

        return max_value if max_value > 0 else 0