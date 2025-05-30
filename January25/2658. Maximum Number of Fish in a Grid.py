# You are given a 0-indexed 2D matrix grid of size m x n, where (r, c) represents:
#
# A land cell if grid[r][c] = 0, or
# A water cell containing grid[r][c] fish, if grid[r][c] > 0.
# A fisher can start at any water cell (r, c) and can do the following operations any number of times:
#
# Catch all the fish at cell (r, c), or
# Move to any adjacent water cell.
# Return the maximum number of fish the fisher can catch if he chooses his starting cell optimally, or 0 if no water cell exists.
#
# An adjacent cell of the cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) or (r - 1, c) if it exists.

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        m = len(grid)
        n = len(grid[0])
        maxFish = 0

        def dfs(i: int, j: int, m: int, n: int) -> int:
            fish = 0

            if grid[i][j] == 0:
                return fish

            fish += grid[i][j]
            grid[i][j] = -1  # Visited

            for dir in directions:
                nr = i + dir[0]
                nc = j + dir[1]
                if 0 <= nr < m and 0 <= nc < n:
                    if grid[nr][nc] > 0:
                        fish += dfs(nr, nc, m, n)

            return fish

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                maxFish = max(maxFish, dfs(i, j, m, n))

        return maxFish