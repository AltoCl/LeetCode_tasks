# Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.
#
# Return the sorted array.

class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        count: list[int] = [0 for _ in range(201)]
        for num in nums:
            count[num + 100] += 1
        nums.sort(key=lambda val: (count[val + 100], -val))
        return nums