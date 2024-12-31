# You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array days. Each day is an integer from 1 to 365.
#
# Train tickets are sold in three different ways:
#
# a 1-day pass is sold for costs[0] dollars,
# a 7-day pass is sold for costs[1] dollars, and
# a 30-day pass is sold for costs[2] dollars.
# The passes allow that many days of consecutive travel.
#
# For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.
# Return the minimum number of dollars you need to travel every day in the given list of days.

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        left7 = 0
        left30 = 0
        dp = [0] * n

        for right in range(n):
            while days[right] - days[left7] >= 7:
                left7 += 1
            while days[right] - days[left30] >= 30:
                left30 += 1

            cost1 = (dp[right - 1] if right > 0 else 0) + costs[0]
            cost7 = (dp[left7 - 1] if left7 > 0 else 0) + costs[1]
            cost30 = (dp[left30 - 1] if left30 > 0 else 0) + costs[2]

            dp[right] = min(cost1, cost7, cost30)

        return dp[n - 1]