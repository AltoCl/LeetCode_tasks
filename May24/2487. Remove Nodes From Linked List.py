#You are given the head of a linked list.
#Remove every node which has a node with a greater value anywhere to the right side of it.
#Return the head of the modified linked list.


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        current = head
        while current:
            while stack and stack[-1].val < current.val:
                stack.pop()
            stack.append(current)
            current = current.next
        dummy = ListNode(0)
        prev = dummy
        for node in stack:
            prev.next = node
            prev = prev.next
        prev.next = None
        return dummy.next