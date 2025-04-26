# You are given an integer array nums and two integers minK and maxK.
#
# A fixed-bound subarray of nums is a subarray that satisfies the following conditions:
#
# The minimum value in the subarray is equal to minK.
# The maximum value in the subarray is equal to maxK.
# Return the number of fixed-bound subarrays.
#
# A subarray is a contiguous part of an array.

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        pMin = pMax = bad = -1
        ans = 0

        for i, num in enumerate(nums):
            if num == minK:
                pMin = i
            if num == maxK:
                pMax = i
            if num < minK or num > maxK:
                bad = i
            if pMin != -1 and pMax != -1:
                ans += max(0, min(pMin, pMax) - bad)

        return ans