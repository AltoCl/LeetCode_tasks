# You are given two integers m and n, which represent the dimensions of a matrix.
#
# You are also given the head of a linked list of integers.
#
# Generate an m x n matrix that contains the integers in the linked list presented in spiral order (clockwise), starting from the top-left of the matrix. If there are remaining empty spaces, fill them with -1.
#
# Return the generated matrix.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        mat = [[-1] * n for _ in range(m)]
        top, left, right, bottom = 0, 0, n - 1, m - 1
        while 1:
            for i in range(left, right + 1):
                if not head:
                    return mat
                mat[top][i] = head.val
                head = head.next
            top += 1

            for i in range(top, bottom + 1):
                if not head:
                    return mat
                mat[i][right] = head.val
                head = head.next
            right -= 1

            for i in range(right, left - 1, -1):
                if not head:
                    return mat
                mat[bottom][i] = head.val
                head = head.next
            bottom -= 1

            for i in range(bottom, top - 1, -1):
                if not head:
                    return mat
                mat[i][left] = head.val
                head = head.next
            left += 1

            if top > bottom or left > right:
                return mat