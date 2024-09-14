# You are given an integer array nums of size n.
#
# Consider a non-empty subarray from nums that has the maximum possible bitwise AND.
#
# In other words, let k be the maximum value of the bitwise AND of any subarray of nums. Then, only subarrays with a bitwise AND equal to k should be considered.
# Return the length of the longest such subarray.
#
# The bitwise AND of an array is the bitwise AND of all the numbers in it.
#
# A subarray is a contiguous sequence of elements within an array.


class Solution(object):
    def longestSubarray(self, nums):
        ans, cnt = 0, 0

        max_element = max(nums)
        for num in nums:
            if num == max_element:
                cnt += 1
            else:
                cnt = 0
            ans = max(ans, cnt)
        return ans