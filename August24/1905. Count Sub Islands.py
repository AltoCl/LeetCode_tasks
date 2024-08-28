# You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.
#
# An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.
#
# Return the number of islands in grid2 that are considered sub-islands.


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n, res = len(grid1), len(grid1[0]), 0

        def dfs(r, c):
            if r < 0 or c < 0 or r == m or c == n or grid2[r][c] == 0:
                return True
            elif grid2[r][c] != grid1[r][c]:
                return False
            grid2[r][c] = 0
            return dfs(r + 1, c) & dfs(r - 1, c) & dfs(r, c + 1) & dfs(r, c - 1)

        return sum(dfs(i, j) for i in range(m) for j in range(n) if grid1[i][j] + grid2[i][j] == 2)