# You are given two integers m and n. Consider an m x n grid where each cell is initially white. You can paint each cell red, green, or blue. All cells must be painted.
#
# Return the number of ways to color the grid with no two adjacent cells having the same color. Since the answer can be very large, return it modulo 109 + 7.


class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        pat = []
        col = [0, 1, 2]

        def dfs(x, s):
            if x == m:
                pat.append(s)
                return
            for i in col:
                if x == 0 or s[x - 1] != i:
                    dfs(x + 1, s + [i])

        dfs(0, [])

        # till this step, we find all valid patterns for a column and store it in the pattern list.

        l = len(pat)
        valid = [[True for _ in range(l)] for _ in range(l)]

        for i in range(l):
            for j in range(i + 1, l):
                for k in range(m):
                    if pat[i][k] == pat[j][k]:
                        valid[i][j] = False
                        break

        # till this step, we find all the pattern pairs that is valid.

        dp = [[0 for _ in range(l)] for _ in range(n)]
        mod = 1_000_000_007
        for i in range(l):
            dp[0][i] = 1

        # for column 0, each pattern is valid.

        for i in range(1, n):
            for x in range(l):
                for y in range(x + 1, l):
                    if valid[x][y]:
                        dp[i][x] = (dp[i][x] + dp[i - 1][y]) % mod
                        dp[i][y] = (dp[i][y] + dp[i - 1][x]) % mod

        # we elaborate to the next column according to the DP formula.

        ans = 0
        for i in range(l):
            ans = (ans + dp[-1][i]) % mod

        # finally, we add up all the answers.

        return ans