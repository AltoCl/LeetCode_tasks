# A critical point in a linked list is defined as either a local maxima or a local minima.
#
# A node is a local maxima if the current node has a value strictly greater than the previous node and the next node.
#
# A node is a local minima if the current node has a value strictly smaller than the previous node and the next node.
#
# Note that a node can only be a local maxima/minima if there exists both a previous node and a next node.
#
# Given a linked list head, return an array of length 2 containing [minDistance, maxDistance] where minDistance is the minimum distance between any two distinct critical points and maxDistance is the maximum distance between any two distinct critical points. If there are fewer than two critical points, return [-1, -1].


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        res = [-1, -1]
        prev_critical_ind = None
        first_critical_ind = None
        prev = head
        cur = head.next
        cur_ind = 1

        while cur.next:
            if (cur.val > prev.val and cur.val > cur.next.val) or (cur.val < prev.val and cur.val < cur.next.val):
                print(cur_ind)
                if prev_critical_ind is not None:
                    res[0] = min(res[0], cur_ind - prev_critical_ind) if res[0] != -1 else cur_ind - prev_critical_ind
                else:
                    first_critical_ind = cur_ind
                prev_critical_ind = cur_ind

            prev = cur
            cur = cur.next
            cur_ind += 1

        if prev_critical_ind != first_critical_ind:
            res[1] = prev_critical_ind - first_critical_ind

        return res