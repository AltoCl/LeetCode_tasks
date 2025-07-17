# You are given an integer array nums and a positive integer k.
# A subsequence sub of nums with length x is called valid if it satisfies:
#
# (sub[0] + sub[1]) % k == (sub[1] + sub[2]) % k == ... == (sub[x - 2] + sub[x - 1]) % k.
# Return the length of the longest valid subsequence of nums.


class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
        # Step 1: Create a 2D DP table to track remainder transitions
        dp = [[0] * k for _ in range(k)]  # dp[prev_rem][curr_rem]
        maxLength = 0

        # Step 2: Loop through each number in the array
        for num in nums:
            current_rem = num % k

            # Step 3: Try to extend existing sequences
            for prev_rem in range(k):
                # Step 4: Update the DP table if a transition is possible
                dp[prev_rem][current_rem] = dp[current_rem][prev_rem] + 1

                # Step 5: Track the longest subsequence found so far
                maxLength = max(maxLength, dp[prev_rem][current_rem])

        # Step 6: Return the maximum length found
        return maxLength