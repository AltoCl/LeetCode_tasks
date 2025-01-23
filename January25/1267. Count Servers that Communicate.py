# You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.
#
# Return the number of servers that communicate with any other server.

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        Rows = [sum(row) for row in grid]
        Col = [sum(grid[i][j] for i in range(len(grid))) for j in range(len(grid[0]))]
        return sum(1 for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 1 and (Rows[i] > 1 or Col[j] > 1))