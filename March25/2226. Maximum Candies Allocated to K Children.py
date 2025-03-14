# You are given a 0-indexed integer array candies. Each element in the array denotes a pile of candies of size candies[i]. You can divide each pile into any number of sub piles, but you cannot merge two piles together.
#
# You are also given an integer k. You should allocate piles of candies to k children such that each child gets the same number of candies. Each child can be allocated candies from only one pile of candies and some piles of candies may go unused.
#
# Return the maximum number of candies each child can get.


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def get_c(c, k):
            for x in candies:
                k -= x // c
                if k <= 0:
                    return True
            return False

        Sum = sum(candies)
        if Sum < k:
            return 0
        l, r = 1, Sum // k
        while l < r:
            m = (l + r + 1) // 2
            if get_c(m, k):
                l = m
            else:
                r = m - 1
        return l
