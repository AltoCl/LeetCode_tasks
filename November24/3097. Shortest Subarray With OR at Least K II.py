# You are given an array nums of non-negative integers and an integer k.
#
# An array is called special if the bitwise OR of all of its elements is at least k.
#
# Return the length of the shortest special non-empty
# subarray
#  of nums, or return -1 if no special subarray exists.


class Solution(object):
    def minimumSubarrayLength(self, nums, k):
        ans = float('inf')
        prev = {}
        for num in nums:
            curr = {num: 1}
            for or_val, length in prev.items():
                new_or = or_val | num
                new_length = length + 1
                if new_or not in curr or curr[new_or] > new_length:
                    curr[new_or] = new_length
            for or_val, length in curr.items():
                if or_val >= k:
                    ans = min(ans, length)
            prev = curr
        return -1 if ans == float('inf') else ans