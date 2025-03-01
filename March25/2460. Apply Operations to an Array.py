# You are given a 0-indexed array nums of size n consisting of non-negative integers.
#
# You need to apply n - 1 operations to this array where, in the ith operation (0-indexed), you will apply the following on the ith element of nums:
#
# If nums[i] == nums[i + 1], then multiply nums[i] by 2 and set nums[i + 1] to 0. Otherwise, you skip this operation.
# After performing all the operations, shift all the 0's to the end of the array.
#
# For example, the array [1,0,2,0,0,1] after shifting all its 0's to the end, is [1,2,1,0,0,0].
# Return the resulting array.
#
# Note that the operations are applied sequentially, not all at once.

from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        new_nums = [0] * len(nums)
        count = 0
        i = 0

        while i < len(nums) - 1:
            if nums[i] != 0:
                if nums[i] == nums[i + 1]:
                    new_nums[count] = nums[i] * 2
                    i += 1
                else:
                    new_nums[count] = nums[i]
                count += 1
            i += 1

        if i < len(nums) and nums[i] != 0:
            new_nums[count] = nums[i]

        return new_nums