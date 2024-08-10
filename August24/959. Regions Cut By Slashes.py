# An n x n grid is composed of 1 x 1 squares where each 1 x 1 square consists of a '/', '\', or blank space ' '. These characters divide the square into contiguous regions.
#
# Given the grid grid represented as a string array, return the number of regions.
#
# Note that backslash characters are escaped, so a '\' is represented as '\\'.


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        def build_matrix(grid):
            n, matrix = len(grid), []
            for i in range(n):
                row1 = []
                row2 = []
                for j in range(n):
                    if grid[i][j] == "/":
                        for v in [0, 1]: row1.append(v)
                        for v in [1, 0]: row2.append(v)
                    elif grid[i][j] == "\\":
                        for v in [2, 0]: row1.append(v)
                        for v in [0, 2]: row2.append(v)
                    else:
                        for v in [0, 0]: row2.append(v)
                        for v in [0, 0]: row1.append(v)
                matrix.append(row1)
                matrix.append(row2)
            return matrix

        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(A) or j >= len(A) or A[i][j] != 0: return

            A[i][j] = -1

            # horizontal and vertical dfs
            dfs(i - 1, j)
            dfs(i, j - 1)
            dfs(i + 1, j)
            dfs(i, j + 1)

            # diagonal dfs
            if i > 0 and j > 0 and (A[i - 1][j] != A[i][j - 1] or A[i - 1][j] != 1):
                dfs(i - 1, j - 1)
            if j > 0 and i < len(A) - 1 and (A[i][j - 1] != A[i + 1][j] or A[i][j - 1] != 2):
                dfs(i + 1, j - 1)
            if i < len(A) - 1 and j < len(A) - 1 and (A[i][j + 1] != A[i + 1][j] or A[i][j + 1] != 1):
                dfs(i + 1, j + 1)
            if j < len(A) - 1 and i > 0 and (A[i][j + 1] != A[i - 1][j] or A[i][j + 1] != 2):
                dfs(i - 1, j + 1)

        res = 0
        A   = build_matrix(grid)
        for i in range(len(A)):
            for j in range(len(A)):
                if A[i][j] == 0:
                    res += 1
                    dfs(i, j)
        return res