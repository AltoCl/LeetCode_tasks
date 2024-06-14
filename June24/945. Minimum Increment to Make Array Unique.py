class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                c = nums[i - 1] - nums[i] + 1
                ans += c
                nums[i] = nums[i - 1] + 1
        # print(nums)
        return ans
