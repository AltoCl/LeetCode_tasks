# There is a dungeon with n x m rooms arranged as a grid.
#
# You are given a 2D array moveTime of size n x m, where moveTime[i][j] represents the minimum time in seconds when you can start moving to that room. You start from the room (0, 0) at time t = 0 and can move to an adjacent room. Moving between adjacent rooms takes one second for one move and two seconds for the next, alternating between the two.
#
# Return the minimum time to reach the room (n - 1, m - 1).
#
# Two rooms are adjacent if they share a common wall, either horizontally or vertically.

import heapq

class Solution:
    def minTimeToReach(self, moveTime):
        n, m = len(moveTime), len(moveTime[0])
        vis = [[False] * m for _ in range(n)]
        heap = [(0, 0, 0, 0)]
        vis[0][0] = True
        dirs = [(0,1), (1,0), (-1,0), (0,-1)]

        while heap:
            time, moves, r, c = heapq.heappop(heap)
            if r == n - 1 and c == m - 1:
                return time
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and not vis[nr][nc]:
                    vis[nr][nc] = True
                    wait = max(time, moveTime[nr][nc])
                    travel_time = 1 if moves % 2 == 0 else 2
                    heapq.heappush(heap, (wait + travel_time, moves + 1, nr, nc))
        return -1