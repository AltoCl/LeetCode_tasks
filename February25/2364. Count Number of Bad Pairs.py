# You are given a 0-indexed integer array nums. A pair of indices (i, j) is a bad pair if i < j and j - i != nums[j] - nums[i].
#
# Return the total number of bad pairs in nums.

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        freq = {}
        good_pairs = 0

        for i, num in enumerate(nums):
            key = num - i
            good_pairs += freq.get(key, 0)
            freq[key] = freq.get(key, 0) + 1

        n = len(nums)
        return (n * (n - 1)) // 2 - good_pairs