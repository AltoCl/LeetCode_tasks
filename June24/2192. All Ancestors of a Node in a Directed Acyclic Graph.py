# You are given a positive integer n representing the number of nodes of a Directed Acyclic Graph (DAG). The nodes are numbered from 0 to n - 1 (inclusive).
#
# You are also given a 2D integer array edges, where edges[i] = [fromi, toi] denotes that there is a unidirectional edge from fromi to toi in the graph.
#
# Return a list answer, where answer[i] is the list of ancestors of the ith node, sorted in ascending order.
#
# A node u is an ancestor of another node v if u can reach v via a set of edges.

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Reverse Graph -> Finding all children of node
        for i in range(len(edges)):
            edges[i][0], edges[i][1] = edges[i][1], edges[i][0]

        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
        cache = {}

        # DFS with cache (memoization DP)
        def dfs(node):
            if node in cache: return cache[node]
            children = set([node])
            for next_node in graph[node]:
                # Extend the set with all of new children
                children |= dfs(next_node)
            cache[node] = children
            return cache[node]

        res = []
        for i in range(n):
            res_i = dfs(i).copy()
            res_i.remove(i)  # remove its self as a child
            res.append(sorted(list(res_i)))  # output need to be sorted
        return res