# You are given an integer n. There is an undirected graph with n vertices, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting vertices ai and bi.
#
# Return the number of complete connected components of the graph.
#
# A connected component is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.
#
# A connected component is said to be complete if there exists an edge between every pair of its vertices.

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x == root_y:
                return
            if rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            elif rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_y] = root_x
                rank[root_x] += 1

        for u, v in edges:
            union(u, v)

        component_vertices = {}
        component_edges = {}

        for i in range(n):
            root = find(i)
            if root not in component_vertices:
                component_vertices[root] = set()
                component_edges[root] = 0
            component_vertices[root].add(i)

        for u, v in edges:
            root = find(u)
            component_edges[root] += 1

        complete_count = 0
        for root in component_vertices:
            num_vertices = len(component_vertices[root])

            expected_edges = num_vertices * (num_vertices - 1) // 2

            if component_edges[root] == expected_edges:
                complete_count += 1

        return complete_count
