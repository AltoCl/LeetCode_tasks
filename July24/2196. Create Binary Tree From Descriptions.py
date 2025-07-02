# You are given a 2D integer array descriptions where descriptions[i] = [parenti, childi, isLefti] indicates that parenti is the parent of childi in a binary tree of unique values. Furthermore,
#
# If isLefti == 1, then childi is the left child of parenti.
# If isLefti == 0, then childi is the right child of parenti.
# Construct the binary tree described by descriptions and return its root.
#
# The test cases will be generated such that the binary tree is valid.

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        mp = {}
        seen = set()
        for p, c, left in descriptions:
            if p not in mp: mp[p] = TreeNode(p)
            if c not in mp: mp[c] = TreeNode(c)
            if left: mp[p].left = mp[c]
            else: mp[p].right = mp[c]
            seen.add(c)
        for p, _, _ in descriptions:
            if p not in seen: return mp[p]