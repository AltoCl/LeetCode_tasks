# Given an integer array arr, return the number of distinct bitwise ORs of all the non-empty subarrays of arr.
#
# The bitwise OR of a subarray is the bitwise OR of each integer in the subarray. The bitwise OR of a subarray of one integer is that integer.
#
# A subarray is a contiguous non-empty sequence of elements within an array.


class Solution:
    def subarrayBitwiseORs(self, arr):
        res = set()
        cur = set()
        for num in arr:
            cur = {num | x for x in cur} | {num}
            res |= cur
        return len(res)