# You are given a 0-indexed integer array nums. An index i is part of a hill in nums if the closest non-equal neighbors of i are smaller than nums[i]. Similarly, an index i is part of a valley in nums if the closest non-equal neighbors of i are larger than nums[i]. Adjacent indices i and j are part of the same hill or valley if nums[i] == nums[j].
#
# Note that for an index to be part of a hill or valley, it must have a non-equal neighbor on both the left and right of the index.
#
# Return the number of hills and valleys in nums.

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        n, prev, cnt = len(nums), nums[0], 0
        diff = [0, 0]
        i = 0
        while i < n:
            while i < n and prev == nums[i]: i += 1
            if i == n: break
            bigger = 1 if nums[i] > prev else 0
            diff[bigger] = 1
            cnt += diff[bigger] and diff[1 - bigger]
            diff[1 - bigger] = 0
            prev = nums[i]
            i += 1
        return cnt
