# You are given a 0-indexed array nums consisting of positive integers. You can choose two indices i and j, such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].
#
# Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions.

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def digitSum(x):
            sum=0
            while x>0:
                q, r=divmod(x, 10)
                sum+=r
                x=q
            return sum

        maxD=[0]*82
        ans=-1
        for x in nums:
            D=digitSum(x)
            if maxD[D]>0:
                ans=max(ans, maxD[D]+x)
            maxD[D]=max(maxD[D], x)
        return ans