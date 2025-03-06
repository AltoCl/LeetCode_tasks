# You are given a 0-indexed 2D integer matrix grid of size n * n with values in the range [1, n2]. Each integer appears exactly once except a which appears twice and b which is missing. The task is to find the repeating and missing numbers a and b.
#
# Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b.


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        size = n * n

        count = [0] * (size + 1)

        for i in range(n):
            for j in range(n):
                count[grid[i][j]] += 1

        a, b = -1, -1

        for num in range(1, size + 1):
            if count[num] == 2:
                a = num
            elif count[num] == 0:
                b = num

        return [a, b]