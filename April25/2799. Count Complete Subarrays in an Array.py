# You are given an array nums consisting of positive integers.
#
# We call a subarray of an array complete if the following condition is satisfied:
#
# The number of distinct elements in the subarray is equal to the number of distinct elements in the whole array.
# Return the number of complete subarrays.
#
# A subarray is a contiguous non-empty part of an array.


class Solution:
    def countCompleteSubarrays(self, nums):
        distinct_elements = set(nums)
        total_distinct = len(distinct_elements)
        count = 0
        n = len(nums)

        for i in range(n):
            current_set = set()
            for j in range(i, n):
                current_set.add(nums[j])
                if len(current_set) == total_distinct:
                    count += (n - j)
                    break
        return count