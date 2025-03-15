# There are several consecutive houses along a street, each of which has some money inside. There is also a robber, who wants to steal money from the homes, but he refuses to steal from adjacent homes.
#
# The capability of the robber is the maximum amount of money he steals from one house of all the houses he robbed.
#
# You are given an integer array nums representing how much money is stashed in each house. More formally, the ith house from the left has nums[i] dollars.
#
# You are also given an integer k, representing the minimum number of houses the robber will steal from. It is always possible to steal at least k houses.
#
# Return the minimum capability of the robber out of all the possible ways to steal at least k houses.

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        n = len(nums)
        x0 = min(nums)
        xM = max(nums)

        def f(cap):
            steal, i = 0, 0
            while i < n and steal <= k:
                if nums[i] <= cap:
                    steal += 1
                    i += 1
                i += 1
            return steal >= k

        l, r = x0, xM
        while l < r:
            m = (l + r) >> 1
            if f(m):
                r = m
            else:
                l = m + 1
        return l
