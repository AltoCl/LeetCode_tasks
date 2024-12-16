# You are given an integer array nums, an integer k, and an integer multiplier.
#
# You need to perform k operations on nums. In each operation:
#
# Find the minimum value x in nums. If there are multiple occurrences of the minimum value, select the one that appears first.
# Replace the selected minimum value x with x * multiplier.
# Return an integer array denoting the final state of nums after performing all k operations.


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap=[(x, i) for i, x in enumerate(nums)]
        heapify(heap)
        for _ in range(k):
            x, i=heap[0]
            heapreplace(heap, (x*multiplier, i))
        for x, i in heap:
            nums[i]=x
        return nums