# Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.
#
# Return the decimal value of the number in the linked list.
#
# The most significant bit is at the head of the linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        curr=head
        v=''
        while curr:
            v+=str(curr.val)
            curr=curr.next
        v=list(v)
        v=v[::-1]
        s=0
        for i in range(len(v)):
            if int(v[i])==1:
                s+=(1<<i)

        return s
