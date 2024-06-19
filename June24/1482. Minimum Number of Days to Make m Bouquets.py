# You are given an integer array bloomDay, an integer m and an integer k.
#
# You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.
#
# The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.
#
# Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        def helper(day: int)-> bool:

            s = ''.join(['X' if b <= day else
                                     ' ' for b in bloomDay])
            return s.count('X'*k) >= m


        n, mn, mx = len(bloomDay), min(bloomDay), max(bloomDay)+1
        if n < m * k: return -1

        return mn + bisect_left(range(mn, mx), True, key = helper)