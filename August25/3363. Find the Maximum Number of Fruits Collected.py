# There is a game dungeon comprised of n x n rooms arranged in a grid.
# #
# # You are given a 2D array fruits of size n x n, where fruits[i][j] represents the number of fruits in the room (i, j). Three children will play in the game dungeon, with initial positions at the corner rooms (0, 0), (0, n - 1), and (n - 1, 0).
# #
# # The children will make exactly n - 1 moves according to the following rules to reach the room (n - 1, n - 1):
# #
# # The child starting from (0, 0) must move from their current room (i, j) to one of the rooms (i + 1, j + 1), (i + 1, j), and (i, j + 1) if the target room exists.
# # The child starting from (0, n - 1) must move from their current room (i, j) to one of the rooms (i + 1, j - 1), (i + 1, j), and (i + 1, j + 1) if the target room exists.
# # The child starting from (n - 1, 0) must move from their current room (i, j) to one of the rooms (i - 1, j + 1), (i, j + 1), and (i + 1, j + 1) if the target room exists.
# # When a child enters a room, they will collect all the fruits there. If two or more children enter the same room, only one child will collect the fruits, and the room will be emptied after they leave.
# #
# # Return the maximum number of fruits the children can collect from the dungeon.

class Solution:
    def maxCollectedFruits(self, mat: List[List[int]]) -> int:
        self.n = len(mat)

        # row = i, col = j
        def dfs3(row, col):
            if row < 0 or col < 0 or row >= self.n or col >= self.n:
                return 0

            val = mat[row][col]
            res = 0

            if row == col:
                res = max(res, dfs3(row + 1, col + 1))
            elif row - 1 == col:
                res = max(res, dfs3(row + 1, col + 1))
                res = max(res, dfs3(row, col + 1))
            else:
                res = max(res, dfs3(row + 1, col + 1))
                res = max(res, dfs3(row, col + 1))
                res = max(res, dfs3(row - 1, col + 1))

            return val + res

        def dfs2(row, col):
            if row < 0 or col < 0 or row >= self.n or col >= self.n:
                return 0

            val = mat[row][col]
            res = 0

            if row == col:
                res = max(res, dfs2(row + 1, col + 1))
            elif row == col - 1:
                res = max(res, dfs2(row + 1, col + 1))
                res = max(res, dfs2(row + 1, col))
            else:
                res = max(res, dfs2(row + 1, col + 1))
                res = max(res, dfs2(row + 1, col))
                res = max(res, dfs2(row + 1, col - 1))

            return val + res

        total = 0

        # child - 1
        # he will eat all diagonal fruits, so set them to 0
        for i in range(self.n):
            total += mat[i][i]
            mat[i][i] = 0

        # child - 2
        total += dfs3(self.n - 1, 0)
        # child - 3
        total += dfs2(0, self.n - 1)

        return total