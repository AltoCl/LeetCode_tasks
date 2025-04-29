# You are given an integer array nums and a positive integer k.
#
# Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.
#
# A subarray is a contiguous sequence of elements within an array.

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_el = max(nums)
        count = 0
        l = 0
        max_found = 0
        n = len(nums)

        for r in range(n):
            if nums[r] == max_el:
                max_found += 1

            while max_found == k:
                count += n - r
                if nums[l] == max_el:
                    max_found -= 1
                l += 1

        return count