# You are given an integer array nums.
#
# You are allowed to delete any number of elements from nums without making it empty. After performing the deletions, select a subarray of nums such that:
#
# All elements in the subarray are unique.
# The sum of the elements in the subarray is maximized.
# Return the maximum sum of such a subarray.

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        sum = 0
        st = set()
        mxNeg = float('-inf')
        for i in range(len(nums)):
            if nums[i] > 0:
                st.add(nums[i])
            else:
                mxNeg = max(mxNeg, nums[i])
        for val in st:
            sum += val
        if len(st) > 0:
            return sum
        else:
            return mxNeg