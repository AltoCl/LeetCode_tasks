# We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.
#
# Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        c = Counter(nums)
        return max(
            0 if c[num + 1] == 0 else freq + c[num + 1]
            for num, freq
            in c.items()
        )