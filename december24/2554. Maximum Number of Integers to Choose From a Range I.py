# You are given an integer array banned and two integers n and maxSum. You are choosing some number of integers following the below rules:
#
# The chosen integers have to be in the range [1, n].
# Each integer can be chosen at most once.
# The chosen integers should not be in the array banned.
# The sum of the chosen integers should not exceed maxSum.
# Return the maximum number of integers you can choose following the mentioned rules.


class Solution:
    def maxCount(self, banned: list[int], n: int, maxSum: int) -> int:
        banned_set = set(banned)  # Use a set for quick lookups
        total_sum = 0  # Track the cumulative sum
        count = 0  # Track the count of valid numbers

        for i in range(1, n + 1):
            if i in banned_set:
                continue  # Skip banned numbers
            total_sum += i
            if total_sum > maxSum:
                break  # Stop if the sum exceeds maxSum
            count += 1

        return count