# Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.
#
# A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        sorted_ans = []

        def inorder_traversal(root):
            if root == None:
                return
            inorder_traversal(root.left)
            sorted_ans.append(root.val)
            inorder_traversal(root.right)
            return

        inorder_traversal(root)
        # lets create the tree
        n = len(sorted_ans)

        def make_tree(low, high):
            if low > high:
                return
            mid = (low + high) // 2
            root = TreeNode(sorted_ans[mid])
            root.left = make_tree(low, mid - 1)
            root.right = make_tree(mid + 1, high)
            return root

        return make_tree(0, n - 1)
