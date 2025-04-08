# You are given an integer array nums. You need to ensure that the elements in the array are distinct. To achieve this, you can perform the following operation any number of times:
#
# Remove 3 elements from the beginning of the array. If the array has fewer than 3 elements, remove all remaining elements.
# Note that an empty array is considered to have distinct elements. Return the minimum number of operations needed to make the elements in the array distinct.


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        while len(nums) > len(set(nums)):
            nums = nums[3:]
            count += 1
        return count

