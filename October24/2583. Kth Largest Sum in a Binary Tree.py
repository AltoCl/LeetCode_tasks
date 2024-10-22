# You are given the root of a binary tree and a positive integer k.
#
# The level sum in the tree is the sum of the values of the nodes that are on the same level.
#
# Return the kth largest level sum in the tree (not necessarily distinct). If there are fewer than k levels in the tree, return -1.
#
# Note that two nodes are on the same level if they have the same distance from the root.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: TreeNode, k: int) -> int:
        res = []  # To store sum of each level
        q = deque([root])  # Queue for level-order traversal (BFS)

        while q:
            n = len(q)  # Number of nodes at the current level
            level_sum = 0  # Sum of node values at the current level

            for _ in range(n):
                node = q.popleft()
                level_sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(level_sum)  # Store the sum of the current level

        if k > len(res):
            return -1

        res.sort(reverse=True)  # Sort the level sums in descending order

        return res[k - 1]  # Return the k-th largest sum