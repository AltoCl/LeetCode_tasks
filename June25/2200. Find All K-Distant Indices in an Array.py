# You are given a 0-indexed integer array nums and two integers key and k. A k-distant index is an index i of nums for which there exists at least one index j such that |i - j| <= k and nums[j] == key.
#
# Return a list of all k-distant indices sorted in increasing order.

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        ans = []
        j = 0
        for i, x in enumerate(nums):
            if x == key:
                up = min(n - 1, i + k)
                j = max(j, i - k)
                while j <= up:
                    ans.append(j)
                    j += 1
        return ans

