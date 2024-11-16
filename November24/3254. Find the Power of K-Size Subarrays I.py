# You are given an array of integers nums of length n and a positive integer k.
#
# The power of an array is defined as:
#
# Its maximum element if all of its elements are consecutive and sorted in ascending order.
# -1 otherwise.
# You need to find the power of all
# subarrays
#  of nums of size k.
#
# Return an integer array results of size n - k + 1, where results[i] is the power of nums[i..(i + k - 1)].


from typing import List


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = [-1] * (n - k + 1)
        i, j = 0, 0

        while j < n:
            if j > 0 and nums[j] - nums[j - 1] != 1:
                i = j
            while i < j and j - i + 1 > k:
                i += 1
            if j - i + 1 == k:
                ans[j - k + 1] = nums[j]
            j += 1

        return ans