# You are given a string word and an integer k.
#
# We consider word to be k-special if |freq(word[i]) - freq(word[j])| <= k for all indices i and j in the string.
#
# Here, freq(x) denotes the frequency of the character x in word, and |y| denotes the absolute value of y.
#
# Return the minimum number of characters you need to delete to make word k-special.


from collections import Counter
import bisect

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        # Step 1: Count character frequencies
        freq = sorted(Counter(word).values())

        # Step 2: Sort frequencies (already done above)
        n = len(freq)

        # Step 3: Compute prefix sum
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + freq[i]

        total = prefix[-1]
        min_del = float('inf')

        # Step 4: Try every frequency as target
        for i in range(n):
            target = freq[i]
            max_allowed = target + k

            # Step 5: Use binary search to find upper bound
            j = bisect.bisect_right(freq, max_allowed)

            # Step 6: Compute deletions
            delete_below = prefix[i]
            delete_above = total - prefix[j] - (max_allowed * (n - j))
            deletions = delete_below + delete_above

            min_del = min(min_del, deletions)

        return min_del