# Given an integer array nums of unique elements, return all possible
# subsets
#  (the power set).
#
# The solution set must not contain duplicate subsets. Return the solution in any order.

def subsets(self, nums: List[int]) -> List[List[int]]:
    n = len(nums)
    ans = []
    subset = []

    def dfs(i):
        if i >= n:
            ans.append(subset.copy())
            return
        subset.append(nums[i])
        dfs(i + 1)
        subset.pop()
        dfs(i + 1)

    dfs(0)
    return ans
