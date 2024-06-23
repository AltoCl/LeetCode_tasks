# Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that
# the absolute difference between any two elements of this subarray is less than or equal to limit.

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minN = deque()
        maxN = deque()

        res = 0
        l = 0

        for r in range(len(nums)):
            while minN and minN[-1][0] >= nums[r]:
                minN.pop()
            while maxN and maxN[-1][0] <= nums[r]:
                maxN.pop()

            minN.append((nums[r], r))
            maxN.append((nums[r], r))

            while maxN and minN and maxN[0][0] - minN[0][0] > limit:
                l = min(maxN[0][1], minN[0][1]) + 1
                if maxN[0][1] == l - 1:
                    maxN.popleft()
                if minN[0][1] == l - 1:
                    minN.popleft()

            res = max(res, r - l + 1)

        return res