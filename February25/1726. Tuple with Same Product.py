#Given an array nums of distinct positive integers, return the number of tuples (a, b, c, d) such that a * b = c * d where a, b, c, and d are elements of nums, and a != b != c!= d.


class Solution:
    def tupleSameProduct(self, nums: list[int]) -> int:

        ans = 0
        count = collections.Counter()

        for i in range(len(nums)):
            for j in range(i):
                prod = nums[i] * nums[j]
                ans += count[prod] * 8
                count[prod] += 1

        return ans