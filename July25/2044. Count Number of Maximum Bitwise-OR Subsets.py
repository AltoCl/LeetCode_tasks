# Given an integer array nums, find the maximum possible bitwise OR of a subset of nums and return the number of different non-empty subsets with the maximum bitwise OR.
#
# An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b. Two subsets are considered different if the indices of the elements chosen are different.
#
# The bitwise OR of an array a is equal to a[0] OR a[1] OR ... OR a[a.length - 1] (0-indexed).


from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # Step 1: Find the maximum possible bitwise OR of the entire array
        max_or = 0
        for num in nums:
            max_or |= num

        # Step 2: Helper function to recursively explore subsets and count those with max OR
        def backtrack(index, current_or):
            if index == len(nums):
                return 1 if current_or == max_or else 0
            # Case 1: Include the current element in the subset
            include = backtrack(index + 1, current_or | nums[index])
            # Case 2: Exclude the current element from the subset
            exclude = backtrack(index + 1, current_or)
            return include + exclude

        # Step 3: Start backtracking from index 0 and initial OR value 0
        return backtrack(0, 0)