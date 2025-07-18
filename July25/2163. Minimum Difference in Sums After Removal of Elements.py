# You are given a 0-indexed integer array nums consisting of 3 * n elements.
#
# You are allowed to remove any subsequence of elements of size exactly n from nums. The remaining 2 * n elements will be divided into two equal parts:
#
# The first n elements belonging to the first part and their sum is sumfirst.
# The next n elements belonging to the second part and their sum is sumsecond.
# The difference in sums of the two parts is denoted as sumfirst - sumsecond.
#
# For example, if sumfirst = 3 and sumsecond = 2, their difference is 1.
# Similarly, if sumfirst = 2 and sumsecond = 3, their difference is -1.
# Return the minimum difference possible between the sums of the two parts after the removal of n elements.

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        diff = [0] * (n + 1)
        heapify(pqL := [-x for x in nums[:n]])
        heapify(pqR := nums[2 * n:])
        Sum = sum(nums[:n])
        ans = Sum
        for i in range(n, 2 * n + 1):
            diff[i - n] = Sum
            x = nums[i]
            if x >= -pqL[0]: continue
            Sum += x + pqL[0]
            heapreplace(pqL, -x)
        Sum = sum(nums[2 * n:])
        ans -= Sum
        for i in range(2 * n - 1, n - 2, -1):
            diff[i - n + 1] -= Sum
            ans = min(ans, diff[i - n + 1])
            x = nums[i]
            if x <= pqR[0]: continue
            Sum += x - pqR[0]
            heapreplace(pqR, x)
        return ans
