# Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.
#
# Return the number of nice sub-arrays.

class Solution(object):
    def numberOfSubarrays(self, nums, k):
        n = len(nums)
        cnt = [0] * (n + 1)
        cnt[0] = 1
        ans = 0
        t = 0
        for v in nums:
            t += v & 1
            if t - k >= 0:
                ans += cnt[t - k]
            cnt[t] += 1
        return ans