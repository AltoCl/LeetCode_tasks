# You are given a 0-indexed integer array nums and an integer pivot. Rearrange nums such that the following conditions are satisfied:
#
# Every element less than pivot appears before every element greater than pivot.
# Every element equal to pivot appears in between the elements less than and greater than pivot.
# The relative order of the elements less than pivot and the elements greater than pivot is maintained.
# More formally, consider every pi, pj where pi is the new position of the ith element and pj is the new position of the jth element. If i < j and both elements are smaller (or larger) than pivot, then pi < pj.
# Return nums after the rearrangement.


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        result = [0] * len(nums)
        left = 0
        right = len(nums) - 1

        for i, j in zip(range(len(nums)), range(len(nums) - 1, -1, -1)):
            if nums[i] < pivot:
                result[left] = nums[i]
                left += 1

            if nums[j] > pivot:
                result[right] = nums[j]
                right -= 1

        while left <= right:
            result[left] = pivot
            left += 1

        return result