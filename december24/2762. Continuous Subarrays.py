# You are given a 0-indexed integer array nums. A subarray of nums is called continuous if:
#
# Let i, i + 1, ..., j be the indices in the subarray. Then, for each pair of indices i <= i1, i2 <= j, 0 <= |nums[i1] - nums[i2]| <= 2.
# Return the total number of continuous subarrays.
#
# A subarray is a contiguous non-empty sequence of elements within an array.

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        l, res = 0, 0
        minD, maxD = deque(), deque()

        for r in range(len(nums)):
            while minD and nums[minD[-1]] >= nums[r]: minD.pop()
            while maxD and nums[maxD[-1]] <= nums[r]: maxD.pop()
            minD.append(r)
            maxD.append(r)

            while nums[maxD[0]] - nums[minD[0]] > 2:
                l += 1
                if minD[0] < l: minD.popleft()
                if maxD[0] < l: maxD.popleft()

            res += r - l + 1

        return res