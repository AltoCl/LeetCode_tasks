# The distance of a pair of integers a and b is defined as the absolute difference between a and b.
#
# Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def countPairs(nums, mid):
            count = 0
            left = 0
            for right in range(len(nums)):
                while nums[right] - nums[left] > mid:
                    left += 1
                count += right - left
            return count

        nums.sort()
        left, right = 0, nums[-1] - nums[0]

        while left < right:
            mid = (left + right) // 2
            count = countPairs(nums, mid)

            if count < k:
                left = mid + 1
            else:
                right = mid

        return left