# You are given three integers n, m, k. A good array arr of size n is defined as follows:
#
# Each element in arr is in the inclusive range [1, m].
# Exactly k indices i (where 1 <= i < n) satisfy the condition arr[i - 1] == arr[i].
# Return the number of good arrays that can be formed.
#
# Since the answer may be very large, return it modulo 109 + 7.


class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        return m*pow(m-1, n-k-1, mod:=10**9+7)*comb(n-1, k)%mod