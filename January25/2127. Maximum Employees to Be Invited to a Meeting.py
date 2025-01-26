# A company is organizing a meeting and has a list of n employees, waiting to be invited. They have arranged for a large circular table, capable of seating any number of employees.
#
# The employees are numbered from 0 to n - 1. Each employee has a favorite person and they will attend the meeting only if they can sit next to their favorite person at the table. The favorite person of an employee is not themself.
#
# Given a 0-indexed integer array favorite, where favorite[i] denotes the favorite person of the ith employee, return the maximum number of employees that can be invited to the meeting.


class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        adj = defaultdict(list)
        transpose = defaultdict(list)
        # first we apply kosaraju, its a cycle, it is that answer itself
        # or we can combine multiple 2 sized connected components (if 0's fav is 1 and 1s fav is 0) ->one exception case to consider
        # max of both the above conditions
        for i in range(len(favorite)):
            adj[i].append(favorite[i])
            transpose[favorite[i]].append(i)

        stack = []
        visited = [False] * len(favorite)

        def dfs(node):
            visited[node] = True
            for n in adj[node]:
                if not visited[n]:
                    dfs(n)
            stack.append(node)

        for i in range(len(favorite)):
            if not visited[i]:
                dfs(i)

        sccs = []  # list of sets of each scc
        scc = set()
        visited = [False] * len(favorite)

        def traverseForScc(node):
            visited[node] = True
            scc.add(node)
            for n in transpose[node]:
                if not visited[n]:
                    traverseForScc(n)

        while stack:
            top = stack.pop()
            if not visited[top]:
                scc = set()
                traverseForScc(top)
                sccs.append(scc)

        ans = max([len(scc) if len(scc) != 2 else -1 for scc in sccs])

        # above was from kosaraju

        def findLongestArm(a, b):
            l = 0
            for node in transpose[a]:
                if node != b:
                    l = max(l, 1 + findLongestArm(node, b))
            return l

        twoNodeSccs = 0
        for n1, n2 in [scc for scc in sccs if len(scc) == 2]:
            twoNodeSccs += 2 + findLongestArm(n1, n2) + findLongestArm(n2, n1)
        return max(ans, twoNodeSccs)