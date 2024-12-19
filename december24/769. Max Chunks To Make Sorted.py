# You are given an integer array arr of length n that represents a permutation of the integers in the range [0, n - 1].
#
# We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.
#
# Return the largest number of chunks we can make to sort the array.

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        return list(accumulate(x-i for i, x in enumerate(arr))).count(0)