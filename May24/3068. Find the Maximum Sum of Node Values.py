# There exists an undirected tree with n nodes numbered 0 to n - 1. You are given a 0-indexed 2D integer array edges of length n - 1, where edges[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the tree. You are also given a positive integer k, and a 0-indexed array of non-negative integers nums of length n, where nums[i] represents the value of the node numbered i.
#
# Alice wants the sum of values of tree nodes to be maximum, for which Alice can perform the following operation any number of times (including zero) on the tree:
#
# Choose any edge [u, v] connecting the nodes u and v, and update their values as follows:
# nums[u] = nums[u] XOR k
# nums[v] = nums[v] XOR k

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        import sys
        n = len(nums)
        cnt = 0
        sac = sys.maxsize
        total_sum = 0

        for num in nums:
            x = num
            y = num ^ k
            if x > y:
                total_sum += x
            else:
                total_sum += y
                cnt += 1
            sac = min(sac, abs(x - y))

        if cnt % 2 == 1:
            total_sum -= sac

        return total_sum