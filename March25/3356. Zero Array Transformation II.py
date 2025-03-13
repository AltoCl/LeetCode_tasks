# You are given an integer array nums of length n and a 2D array queries where queries[i] = [li, ri, vali].
#
# Each queries[i] represents the following action on nums:
#
# Decrement the value at each index in the range [li, ri] in nums by at most vali.
# The amount by which each value is decremented can be chosen independently for each index.
# A Zero Array is an array with all its elements equal to 0.
#
# Return the minimum possible non-negative value of k, such that after processing the first k queries in sequence, nums becomes a Zero Array. If no such k exists, return -1.


class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n, m = len(nums), len(queries)
        freq = [0] * (n + 1)
        op, k = 0, 0
        for i in range(n):
            while op < nums[i] - freq[i]:
                if k >= m:
                    return -1
                l, r, v = queries[k]
                if r < i:
                    k += 1
                    continue
                freq[max(l, i)] += v
                freq[r + 1] -= v
                k += 1
            op += freq[i]
        return k
