# Given an integer array nums and an integer k, return the number of good subarrays of nums.
#
# A subarray arr is good if there are at least k pairs of indices (i, j) such that i < j and arr[i] == arr[j].
#
# A subarray is a contiguous non-empty sequence of elements within an array.


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = defaultdict(int)
        ans, cnt, l = 0, 0, 0
        for r, x in enumerate(nums):
            cnt += freq[x]
            freq[x] += 1
            while cnt >= k:
                ans += n - r
                freq[nums[l]] -= 1
                cnt -= freq[nums[l]]
                l += 1
        return ans

