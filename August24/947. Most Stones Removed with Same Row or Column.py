# On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.
#
# A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.
#
# Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the largest possible number of stones that can be removed.


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def dfs(x):
            visited.add(x)
            for y in graph[x]:
                if y not in visited:
                    dfs(y)

        graph = collections.defaultdict(list)
        for i, (x1, y1) in enumerate(stones):
            for j, (x2, y2) in enumerate(stones):
                if i != j and (x1 == x2 or y1 == y2):
                    graph[i].append(j)

        visited = set()
        components = 0

        for i in range(len(stones)):
            if i not in visited:
                dfs(i)
                components += 1

        return len(stones) - components