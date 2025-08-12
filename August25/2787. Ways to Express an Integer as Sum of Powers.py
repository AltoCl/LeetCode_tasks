# Given two positive integers n and x.
#
# Return the number of ways n can be expressed as the sum of the xth power of unique positive integers, in other words, the number of sets of unique integers [n1, n2, ..., nk] where n = n1x + n2x + ... + nkx.
#
# Since the result can be very large, return it modulo 109 + 7.
#
# For example, if n = 160 and x = 3, one way to express n is n = 23 + 33 + 53.

class Solution:
    M = 10 ** 9 + 7

    def __init__(self):
        self.memo = [[-1] * 301 for _ in range(301)]

    def func(self, n, sum_, x, num):
        if sum_ == n:
            return 1
        tmp = pow(num, x)

        if sum_ + tmp > n:
            return 0

        if self.memo[num][sum_] != -1:  # added
            return self.memo[num][sum_]

        take = self.func(n, sum_ + tmp, x, num + 1)
        not_take = self.func(n, sum_, x, num + 1)

        self.memo[num][sum_] = (take + not_take) % self.M  # updated
        return self.memo[num][sum_]

    def numberOfWays(self, n, x):
        return self.func(n, 0, x, 1)