# Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.
#
# A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:
#
# 0 <= i < j < k < arr.length
# |arr[i] - arr[j]| <= a
# |arr[j] - arr[k]| <= b
# |arr[i] - arr[k]| <= c
# Where |x| denotes the absolute value of x.
#
# Return the number of good triplets.

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        n = len(arr)
        MAX_VALUE = 1000
        prefix_counts = [0] * (MAX_VALUE + 1)

        for j in range(n):
            for k in range(j + 1, n):
                if abs(arr[j] - arr[k]) > b:
                    continue

                lower = max(0, arr[j] - a, arr[k] - c)
                upper = min(MAX_VALUE, arr[j] + a, arr[k] + c)

                if lower > upper:
                    continue

                if lower == 0:
                    valid = prefix_counts[upper]
                else:
                    valid = prefix_counts[upper] - prefix_counts[lower - 1]

                count += valid

            # Update prefix_counts for future queries
            for x in range(arr[j], MAX_VALUE + 1):
                prefix_counts[x] += 1

        return count