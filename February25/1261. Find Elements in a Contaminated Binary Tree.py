# Given a binary tree with the following rules:
#
# root.val == 0
# For any treeNode:
# If treeNode.val has a value x and treeNode.left != null, then treeNode.left.val == 2 * x + 1
# If treeNode.val has a value x and treeNode.right != null, then treeNode.right.val == 2 * x + 2
# Now the binary tree is contaminated, which means all treeNode.val have been changed to -1.
#
# Implement the FindElements class:
#
# FindElements(TreeNode* root) Initializes the object with a contaminated binary tree and recovers it.
# bool find(int target) Returns true if the target value exists in the recovered binary tree.



class FindElements:
    def __init__(self, root):
        self.recoveredValues = set()
        root.val = 0
        self.recoverTree(root)

    def recoverTree(self, root):
        if not root:
            return
        self.recoveredValues.add(root.val)
        if root.left:
            root.left.val = 2 * root.val + 1
            self.recoverTree(root.left)
        if root.right:
            root.right.val = 2 * root.val + 2
            self.recoverTree(root.right)

    def find(self, target):
        return target in self.recoveredValues