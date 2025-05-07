# There is a dungeon with n x m rooms arranged as a grid.
#
# You are given a 2D array moveTime of size n x m, where moveTime[i][j] represents the minimum time in seconds when you can start moving to that room. You start from the room (0, 0) at time t = 0 and can move to an adjacent room. Moving between adjacent rooms takes exactly one second.
#
# Return the minimum time to reach the room (n - 1, m - 1).
#
# Two rooms are adjacent if they share a common wall, either horizontally or vertically.

import heapq

class Solution:
    def minTimeToReach(self, moveTime):
        m, n = len(moveTime), len(moveTime[0])
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0
        heap = [(0, 0, 0)]  # time, row, col

        while heap:
            time, r, c = heapq.heappop(heap)
            if (r, c) == (m-1, n-1):
                return time
            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    wait_time = max(time, moveTime[nr][nc]) + 1
                    if wait_time < dist[nr][nc]:
                        dist[nr][nc] = wait_time
                        heapq.heappush(heap, (wait_time, nr, nc))
        return -1