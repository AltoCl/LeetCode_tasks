# Given a binary array nums, you should delete one element from it.
#
# Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n, l, zeros, ans = len(nums), 0, 0, 0
        for r, x in enumerate(nums):
            zeros += (x == 0)
            if zeros > 1:
                zeros -= (nums[l] == 0)
                l += 1
            ans = max(ans, r - l)
        return ans

