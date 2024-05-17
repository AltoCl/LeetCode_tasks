# Given a binary tree root and an integer target, delete all the leaf nodes with value target.
#
# Note that once you delete a leaf node with value target, if its parent node becomes a leaf node and has the value target, it should also be deleted (you need to continue doing that until you cannot).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, r: Optional[TreeNode], t: int) -> Optional[TreeNode]:
        def f(n):
            if n:
                n.left, n.right = f(n.left), f(n.right)

                return (n, None)[n.left == n.right == None and n.val == t]

        return f(r)