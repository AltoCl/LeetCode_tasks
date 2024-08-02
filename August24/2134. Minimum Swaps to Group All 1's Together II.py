# A swap is defined as taking two distinct positions in an array and swapping the values in them.
#
# A circular array is defined as an array where we consider the first element and the last element to be adjacent.
#
# Given a binary circular array nums, return the minimum number of swaps required to group all 1's present in the array together at any location.

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        k = nums.count(1)
        mx = cnt = sum(nums[:k])
        n = len(nums)
        for i in range(k, n + k):
            cnt += nums[i % n]
            cnt -= nums[(i - k + n) % n]
            mx = max(mx, cnt)
        return k - mx