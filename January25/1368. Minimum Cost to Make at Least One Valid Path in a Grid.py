# Given an m x n grid. Each cell of the grid has a sign pointing to the next cell you should visit if you are currently in this cell. The sign of grid[i][j] can be:
#
# 1 which means go to the cell to the right. (i.e go from grid[i][j] to grid[i][j + 1])
# 2 which means go to the cell to the left. (i.e go from grid[i][j] to grid[i][j - 1])
# 3 which means go to the lower cell. (i.e go from grid[i][j] to grid[i + 1][j])
# 4 which means go to the upper cell. (i.e go from grid[i][j] to grid[i - 1][j])
# Notice that there could be some signs on the cells of the grid that point outside the grid.
#
# You will initially start at the upper left cell (0, 0). A valid path in the grid is a path that starts from the upper left cell (0, 0) and ends at the bottom-right cell (m - 1, n - 1) following the signs on the grid. The valid path does not have to be the shortest.
#
# You can modify the sign on a cell with cost = 1. You can modify the sign on a cell one time only.
#
# Return the minimum cost to make the grid have at least one valid path.

class Solution(object):
    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        # Initialize the minCost matrix with a large value
        minCost = [[float('inf')] * n for _ in range(m)]
        minCost[0][0] = 0

        # Deque for 0-1 BFS
        dque = deque([(0, 0)])

        # Directions: right, left, down, up
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while dque:
            r, c = dque.popleft()

            # Visit adjacent cells
            for i, (dr, dc) in enumerate(directions):
                nr, nc = r + dr, c + dc
                cost = 1 if grid[r][c] != i + 1 else 0

                if 0 <= nr < m and 0 <= nc < n and minCost[r][c] + cost < minCost[nr][nc]:
                    minCost[nr][nc] = minCost[r][c] + cost

                    # Add to deque based on cost
                    if cost == 1:
                        dque.append((nr, nc))
                    else:
                        dque.appendleft((nr, nc))

        # Return the minimum cost to reach the bottom-right corner
        return minCost[m - 1][n - 1]