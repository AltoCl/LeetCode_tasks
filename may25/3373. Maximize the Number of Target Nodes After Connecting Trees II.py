# There exist two undirected trees with n and m nodes, labeled from [0, n - 1] and [0, m - 1], respectively.
#
# You are given two 2D integer arrays edges1 and edges2 of lengths n - 1 and m - 1, respectively, where edges1[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the first tree and edges2[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the second tree.
#
# Node u is target to node v if the number of edges on the path from u to v is even. Note that a node is always target to itself.
#
# Return an array of n integers answer, where answer[i] is the maximum possible number of nodes that are target to node i of the first tree if you had to connect one node from the first tree to another node in the second tree.
#
# Note that queries are independent from each other. That is, for every query you will remove the added edge before proceeding to the next query.


class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        def find_even(edges: list, n : int) -> list:
            graph = [[] for _ in range(n)]
            queue = deque([(0, -1, True)])
            evens = [False] * n
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)
            while queue:
                node, parent, is_even = queue.popleft()
                evens[node] = is_even
                for child in graph[node]:
                    if child == parent:
                        continue
                    queue.append((child, node, not is_even))
            return evens
        n1, n2 = len(edges1) + 1, len(edges2) + 1
        even1, even2 = find_even(edges1, n1), find_even(edges2, n2)
        total1, total2 = sum(even1), sum(even2)
        mx = max(total2, n2 - total2)
        ans = [mx + (total1 if even else n1 - total1) for even in even1]
        return ans
