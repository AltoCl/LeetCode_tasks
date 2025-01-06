# You have n boxes. You are given a binary string boxes of length n, where boxes[i] is '0' if the ith box is empty, and '1' if it contains one ball.
#
# In one operation, you can move one ball from a box to an adjacent box. Box i is adjacent to box j if abs(i - j) == 1. Note that after doing so, there may be more than one ball in some boxes.
#
# Return an array answer of size n, where answer[i] is the minimum number of operations needed to move all the balls to the ith box.
#
# Each answer[i] is calculated considering the initial state of the boxes.


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        distances = [0] * n

        prefixCount = 0
        prefixSum = 0

        for i in range(n):
            distances[i] = prefixCount * i - prefixSum
            if boxes[i] == '1':
                prefixCount += 1
                prefixSum += i

        suffixCount = 0
        suffixSum = 0

        for i in range(n - 1, -1, -1):
            distances[i] += suffixSum - suffixCount * i
            if boxes[i] == '1':
                suffixCount += 1
                suffixSum += i

        return distances