# You are given an array of events where events[i] = [startDayi, endDayi, valuei]. The ith event starts at startDayi and ends at endDayi, and if you attend this event, you will receive a value of valuei. You are also given an integer k which represents the maximum number of events you can attend.
#
# You can only attend one event at a time. If you choose to attend an event, you must attend the entire event. Note that the end day is inclusive: that is, you cannot attend two events where one of them starts and the other ends on the same day.
#
# Return the maximum sum of values that you can receive by attending events.


# import numpy as np
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        N = len(events)
        events.sort()

        memo = [[-1 for _ in range(k + 1)] for _ in range(N)]

        def max_events_recur(idx, k):
            if idx == N or k == 0:
                return 0

            if memo[idx][k] != -1:
                return memo[idx][k]

            startDay, endDay, value = events[idx]

            # Take this event
            # Get the next available event to call recursion on after taking this event
            nextIdxAvail = bisect.bisect_right(events, endDay, key=lambda event: event[0])
            total = value + max_events_recur(nextIdxAvail, k - 1)

            # Don't take this event
            total = max(total, max_events_recur(idx + 1, k))

            memo[idx][k] = total
            return total

        total = max_events_recur(0, k)
        # print("memo: ")
        # print(np.array(memo))
        return total