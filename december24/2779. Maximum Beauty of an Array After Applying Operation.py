# You are given a 0-indexed array nums and a non-negative integer k.
#
# In one operation, you can do the following:
#
# Choose an index i that hasn't been chosen before from the range [0, nums.length - 1].
# Replace nums[i] with any integer from the range [nums[i] - k, nums[i] + k].
# The beauty of the array is the length of the longest subsequence consisting of equal elements.
#
# Return the maximum possible beauty of the array nums after applying the operation any number of times.
#
# Note that you can apply the operation to each index only once.
#
# A subsequence of an array is a new array generated from the original array by deleting some elements (possibly none) without changing the order of the remaining elements.


class Solution:
    def maximumBeauty(self, nums: list[int], k: int) -> int:
        # Extend the range for each element in nums
        events = []
        for num in nums:
            events.append((num - k, 1))  # Start of range
            events.append((num + k + 1, -1))  # End of range (exclusive)

        # Sort events by value, and in case of tie, by type of event
        events.sort()

        # Use a sweep line approach to calculate the maximum overlap
        max_beauty = 0
        current_count = 0
        for value, effect in events:
            current_count += effect
            max_beauty = max(max_beauty, current_count)

        return max_beauty