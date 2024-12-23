# You are given the root of a binary tree with unique values.
#
# In one operation, you can choose any two nodes at the same level and swap their values.
#
# Return the minimum number of operations needed to make the values at each level sorted in a strictly increasing order.
#
# The level of a node is the number of edges along the path between it and the root node.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def dfs(i, idx, viz):
            if viz[i]: return 0
            viz[i]=True
            j=idx[i]
            return 1+dfs(j, idx, viz)

        q=deque()
        q.append(root)
        swaps=0
        while q:
            qz=len(q)
            arr=[0]*qz
            for i in range(qz):
                node=q.popleft()
                arr[i]=node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            idx=sorted(range(qz), key = lambda k : arr[k])

            viz=[False]*qz
            for i in range(qz):
                if not viz[i]:
                    swaps+=dfs(i, idx, viz)-1
        return swaps