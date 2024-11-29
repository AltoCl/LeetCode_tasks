# You are given a m x n matrix grid consisting of non-negative integers where grid[row][col] represents the minimum time required to be able to visit the cell (row, col), which means you can visit the cell (row, col) only when the time you visit it is greater than or equal to grid[row][col].
#
# You are standing in the top-left cell of the matrix in the 0th second, and you must move to any adjacent cell in the four directions: up, down, left, and right. Each move you make takes 1 second.
#
# Return the minimum time required in which you can visit the bottom-right cell of the matrix. If you cannot visit the bottom-right cell, then return -1.

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        MOVES = ((-1, 0), (0, 1), (1, 0), (0, -1))

        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        rows, cols = len(grid), len(grid[0])
        pq = [(0, 0, 0)]  # time, row(x), col(y)
        seen = [[False] * cols for _ in range(rows)]
        seen[0][0] = True

        while pq:
            time, row, col = heappop(pq)

            for dr, dc in MOVES:
                newRow, newCol = row + dr, col + dc

                if (newRow < 0 or newRow >= rows or
                        newCol < 0 or newCol >= cols or
                        seen[newRow][newCol]):
                    continue

                newTime = time + 1
                if grid[newRow][newCol] > newTime:
                    newTime += (grid[newRow][newCol] - time) // 2 * 2

                if newRow == rows - 1 and newCol == cols - 1:
                    return newTime

                seen[newRow][newCol] = True
                heappush(pq, (newTime, newRow, newCol))

        return -1