# Given an array of integers nums, sort the array in ascending order and return it.
#
# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left_half = self.sortArray(nums[:mid])
        right_half = self.sortArray(nums[mid:])
        return self.merge(left_half, right_half)

    def merge(self, left, right):
        sorted_array = []
        left_index, right_index = 0, 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                sorted_array.append(left[left_index])
                left_index += 1
            else:
                sorted_array.append(right[right_index])
                right_index += 1

        while left_index < len(left):
            sorted_array.append(left[left_index])
            left_index += 1

        while right_index < len(right):
            sorted_array.append(right[right_index])
            right_index += 1

        return sorted_array

    def medianOfThree(self, nums, low, mid, high):
        if (nums[low] < nums[mid] and nums[mid] < nums[high]) or (nums[high] < nums[mid] and nums[mid] < nums[low]):
            return mid
        elif (nums[mid] < nums[low] and nums[low] < nums[high]) or (nums[high] < nums[low] and nums[low] < nums[mid]):
            return low
        else:
            return high