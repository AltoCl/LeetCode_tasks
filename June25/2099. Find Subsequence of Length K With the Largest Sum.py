# You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k that has the largest sum.
#
# Return any such subsequence as an integer array of length k.
#
# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.


from typing import List


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # Pair with indices
        nums_with_indices = [(num, i) for i, num in enumerate(nums)]

        # Sort by value descending
        nums_with_indices.sort(key=lambda x: -x[0])

        # Take top k and sort by original index
        top_k = sorted(nums_with_indices[:k], key=lambda x: x[1])

        # Extract values
        return [num for num, _ in top_k]