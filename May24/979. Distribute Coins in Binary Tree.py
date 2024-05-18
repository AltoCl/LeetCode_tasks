# You are given the root of a binary tree with n nodes where each node in the tree has node.val coins. There are n coins in total throughout the whole tree.
#
# In one move, we may choose two adjacent nodes and move one coin from one node to another. A move may be from parent to child, or from child to parent.
#
# Return the minimum number of moves required to make every node have exactly one coin.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.moves = 0

    def distributeCoins(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.moves

    def dfs(self, node: TreeNode) -> int:
        if not node:
            return 0
        left_excess = self.dfs(node.left)
        right_excess = self.dfs(node.right)
        self.moves += abs(left_excess) + abs(right_excess)
        return node.val + left_excess + right_excess - 1