# Given an array of integers arr, return the number of subarrays with an odd sum.
#
# Since the answer can be very large, return it modulo 109 + 7.

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        sum_is_odd=0
        cnt=[1, 0]
        ans=0
        for x in arr:
            sum_is_odd^=(x&1)
            ans+=cnt[1-sum_is_odd]
            cnt[sum_is_odd]+=1
        return ans%(10**9+7)