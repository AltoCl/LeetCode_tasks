# Given an array of integers arr.
#
# We want to select three indices i, j and k where (0 <= i < j <= k < arr.length).
#
# Let's define a and b as follows:
#
# a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
# b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
# Note that ^ denotes the bitwise-xor operation.
#
# Return the number of triplets (i, j and k) Where a == b.

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] ^ arr[i]

        count = 0
        for i in range(n):
            for k in range(i + 1, n):
                if prefix[i] == prefix[k + 1]:
                    count += (k - i)

        return count