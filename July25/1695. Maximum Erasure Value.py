# You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.
#
# Return the maximum score you can get by erasing exactly one subarray.
#
# An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        hasX = [False] * (max(nums) + 1)
        ans, wsum = 0, 0
        l, r = 0, 0
        for l, x in enumerate(nums):
            while r < n and not hasX[(y := nums[r])]:
                hasX[y] = True
                wsum += y
                r += 1
            ans = max(ans, wsum)
            hasX[x] = False
            wsum -= x
            if r >= n - 1: break
        return ans
