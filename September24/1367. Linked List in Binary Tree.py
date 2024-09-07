# Given a binary tree root and a linked list with head as the first node.
#
# Return True if all the elements in the linked list starting from the head correspond to some downward path connected in the binary tree otherwise return False.
#
# In this context downward path means a path that starts at some node and goes downwards.



class Solution:
    def isSubPath(self, head, root):
        def checkPath(head, root):
            if not head: return True
            if not root or head.val != root.val: return False
            return checkPath(head.next, root.left) or checkPath(head.next, root.right)

        if not root: return False
        if checkPath(head, root): return True
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)