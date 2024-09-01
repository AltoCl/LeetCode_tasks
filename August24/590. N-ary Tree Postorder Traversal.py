# Given the root of an n-ary tree, return the postorder traversal of its nodes' values.
#
# Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

class Solution(object):
    def postorder(self, root):
        # If the root is None, return an empty list
        if not root:
            return []

        res = []

        # Define the DFS function
        def dfs(root):
            # Recursively call dfs for each child of the current node
            for x in root.children:
                dfs(x)
            # Append the value of the current node to the result list
            res.append(root.val)

        # Start DFS from the root
        dfs(root)

        # Return the result list containing node values in post-order
        return res