# You are given an integer array nums and an integer target.
#
# You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.
#
# For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
# Return the number of different expressions that you can build, which evaluates to target.


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        Sum = sum(nums)
        diff = Sum - target

        if diff < 0 or diff % 2 == 1: return 0
        diff /= 2

        @cache
        def f(j, sum):
            if j == 0: return 1 if sum == 0 else 0
            x = nums[j - 1]
            ans = f(j - 1, sum)
            if sum >= x:
                ans += f(j - 1, sum - x)
            return ans

        return f(n, diff)
