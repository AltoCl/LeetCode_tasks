# There is an undirected tree with n nodes labeled from 0 to n - 1. You are given the integer n and a 2D integer array edges of length n - 1, where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.
#
# You are also given a 0-indexed integer array values of length n, where values[i] is the value associated with the ith node, and an integer k.
#
# A valid split of the tree is obtained by removing any set of edges, possibly empty, from the tree such that the resulting components all have values that are divisible by k, where the value of a connected component is the sum of the values of its nodes.
#
# Return the maximum number of components in any valid split.

class Solution:
    def maxKDivisibleComponents(self, n, edges, vals, k):
        from collections import deque, defaultdict

        if n < 2:
            return 1

        graph = defaultdict(list)
        degree = [0] * n

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            degree[a] += 1
            degree[b] += 1

        node_vals = vals[:]
        leaf_q = deque([i for i in range(n) if degree[i] == 1])
        comp_cnt = 0

        while leaf_q:
            curr = leaf_q.popleft()
            degree[curr] -= 1
            carry = 0

            if node_vals[curr] % k == 0:
                comp_cnt += 1
            else:
                carry = node_vals[curr]

            for nbr in graph[curr]:
                if degree[nbr] == 0:
                    continue
                degree[nbr] -= 1
                node_vals[nbr] += carry
                if degree[nbr] == 1:
                    leaf_q.append(nbr)

        return comp_cnt