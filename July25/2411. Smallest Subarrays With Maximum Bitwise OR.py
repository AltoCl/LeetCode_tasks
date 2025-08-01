# You are given a 0-indexed array nums of length n, consisting of non-negative integers. For each index i from 0 to n - 1, you must determine the size of the minimum sized non-empty subarray of nums starting at i (inclusive) that has the maximum possible bitwise OR.
#
# In other words, let Bij be the bitwise OR of the subarray nums[i...j]. You need to find the smallest subarray starting at i, such that bitwise OR of this subarray is equal to max(Bik) where i <= k <= n - 1.
# The bitwise OR of an array is the bitwise OR of all the numbers in it.
#
# Return an integer array answer of size n where answer[i] is the length of the minimum sized subarray starting at i with maximum bitwise OR.
#
# A subarray is a contiguous non-empty sequence of elements within an array.


class Solution:
    def smallestSubarrays(self, a: List[int]) -> List[int]:
        return [*map(lambda d:max(d.values())-d[-1]+1,accumulate(range(len(a)-1,-1,-1),
            lambda d,i:d|{q:i for q in range(32) if a[i]&1<<q}|{-1:i},initial={-1:0}))][:0:-1]