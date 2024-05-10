# You are given a sorted integer array arr containing 1 and prime numbers, where all the integers of arr are unique. You are also given an integer k.
# For every i and j where 0 <= i < j < arr.length, we consider the fraction arr[i] / arr[j].
# Return the kth smallest fraction considered. Return your answer as an array of integers of size 2, where answer[0] == arr[i] and answer[1] == arr[j].

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        minHeap = []
        N = len(arr)
        for i in range(N):
            for j in range(i + 1, N):
                fraction = (arr[i] / arr[j], (arr[i], arr[j]))
                heappush(minHeap, fraction)
        for _ in range(k - 1):
            heappop(minHeap)
        return heappop(minHeap)[1]