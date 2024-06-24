# You are given a binary array nums and an integer k.
#
# A k-bit flip is choosing a subarray of length k from nums and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.
#
# Return the minimum number of k-bit flips required so that there is no 0 in the array. If it is not possible, return -1.
#
# A subarray is a contiguous part of an array.

class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        n, flipped, res = len(A), 0, 0
        fp = [0] * n
        for i in range(n):
            if i >= K:
                flipped ^= fp[i - K]
            if flipped == A[i]:
                if i + K > n:
                    return -1
                fp[i] = 1
                flipped ^= 1
                res += 1
        return res