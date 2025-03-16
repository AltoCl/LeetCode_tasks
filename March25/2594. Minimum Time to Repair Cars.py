# You are given an integer array ranks representing the ranks of some mechanics. ranksi is the rank of the ith mechanic. A mechanic with a rank r can repair n cars in r * n2 minutes.
#
# You are also given an integer cars representing the total number of cars waiting in the garage to be repaired.
#
# Return the minimum time taken to repair all the cars.
#
# Note: All the mechanics can repair the cars simultaneously.

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        freq = Counter(ranks)
        minR = min(ranks)

        #    maxR=max(ranks) # no need
        def canRepair(t):
            cnt = 0
            for x, f in freq.items():
                cnt += f * (sqrt(t / x) // 1)
                if cnt >= cars: return True
            return cnt >= cars

        l, r = 1, minR * cars * cars
        while l < r:
            m = (l + r) >> 1
            if canRepair(m):
                r = m
            else:
                l = m + 1
        return l
