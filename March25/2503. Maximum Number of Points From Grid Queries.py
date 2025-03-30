# You are given an m x n integer matrix grid and an array queries of size k.
#
# Find an array answer of size k such that for each integer queries[i] you start in the top left cell of the matrix and repeat the following process:
#
# If queries[i] is strictly greater than the value of the current cell that you are in, then you get one point if it is your first time visiting this cell, and you can move to any adjacent cell in all 4 directions: up, down, left, and right.
# Otherwise, you do not get any points, and you end this process.
# After the process, answer[i] is the maximum number of points you can get. Note that for each query you are allowed to visit the same cell multiple times.
#
# Return the resulting array answer.

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])

        visited = set([(0, 0)])
        visiting = [(0, 0)]
        dropped = []

        scores = {}
        curr_score = 0

        for q in sorted(set(queries)):
            while visiting:
                next_visit = []
                for x, y in visiting:
                    if grid[x][y] < q:
                        curr_score += 1
                        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                            if 0 <= x + dx and m > x + dx and \
                                    0 <= y + dy and n > y + dy and \
                                    (x + dx, y + dy) not in visited:
                                next_visit.append((x + dx, y + dy))
                                visited.add((x + dx, y + dy))
                    else:
                        dropped.append((x, y))
                visiting = next_visit
            scores[q] = curr_score
            visiting = dropped
            dropped = []

        return [scores.get(q, 0) for q in queries]

