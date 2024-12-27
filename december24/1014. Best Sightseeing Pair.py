# You are given an integer array values where values[i] represents the value of the ith sightseeing spot. Two sightseeing spots i and j have a distance j - i between them.
#
# The score of a pair (i < j) of sightseeing spots is values[i] + values[j] + i - j: the sum of the values of the sightseeing spots, minus the distance between them.
#
# Return the maximum score of a pair of sightseeing spots.


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        suffixMax = [0] * n
        suffixMax[n - 1] = values[n - 1] - (n - 1)

        for i in range(n - 2, -1, -1):
            suffixMax[i] = max(suffixMax[i + 1], values[i] - i)

        maxScore = float('-inf')

        for i in range(n - 1):
            maxScore = max(maxScore, values[i] + i + suffixMax[i + 1])

        return maxScore