# You are given an integer n. There are n rooms numbered from 0 to n - 1.
#
# You are given a 2D integer array meetings where meetings[i] = [starti, endi] means that a meeting will be held during the half-closed time interval [starti, endi). All the values of starti are unique.
#
# Meetings are allocated to rooms in the following manner:
#
# Each meeting will take place in the unused room with the lowest number.
# If there are no available rooms, the meeting will be delayed until a room becomes free. The delayed meeting should have the same duration as the original meeting.
# When a room becomes unused, meetings that have an earlier original start time should be given the room.
# Return the number of the room that held the most meetings. If there are multiple rooms, return the room with the lowest number.
#
# A half-closed interval [a, b) is the interval between a and b including a and not including b.

class Solution:
    def mostBooked(self, n: int, m: List[List[int]]) -> int:
        r, c = [0]*n, [0]*n # rooms, counter
        for s, e in sorted(m):
            found = 0
            for i,f in enumerate(r):
                if f <= s:
                    r[i] = e
                    c[i] += 1
                    found = 1
                    break

            if not found:
                q = r.index(min(r))
                r[q] += e-s
                c[q] += 1

        return c.index(max(c))