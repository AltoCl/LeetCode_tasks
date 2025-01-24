# There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].
#
# A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node).
#
# Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        res = []
        visited = set()
        memo = [0] * n

        def dfs(i):
            if memo[i] == 1 or len(graph[i]) == 0:
                return True
            elif memo[i] == -1 or i in visited:
                return False

            visited.add(i)

            for neighbour in graph[i]:
                if not dfs(neighbour):
                    memo[i] = -1
                    return False

            memo[i] = 1
            return True

        for i in range(n):
            if dfs(i):
                res.append(i)

        return res