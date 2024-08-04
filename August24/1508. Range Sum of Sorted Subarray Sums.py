# You are given the array nums consisting of n positive integers. You computed the sum of all non-empty continuous subarrays from the array and then sorted them in non-decreasing order, creating a new array of n * (n + 1) / 2 numbers.
#
# Return the sum of the numbers from index left to index right (indexed from 1), inclusive, in the new array. Since the answer can be a huge number return it modulo 109 + 7.

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        mod = int(1e9 + 7)
        dp = [[] for _ in range(n)]
        dp[-1].append(nums[-1])
        for i in range(n-2,-1,-1):
            val = nums[i]
            dp[i].append(val)
            for ele in dp[i+1]:
                dp[i].append(ele+val)
        ans = []
        for row in dp:ans.extend(row)
        ans.sort()
        return sum(ans[left-1:right])%mod