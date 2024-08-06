# You are given a string word containing lowercase English letters.
#
# Telephone keypads have keys mapped with distinct collections of lowercase English letters, which can be used to form words by pushing them. For example, the key 2 is mapped with ["a","b","c"], we need to push the key one time to type "a", two times to type "b", and three times to type "c" .
#
# It is allowed to remap the keys numbered 2 to 9 to distinct collections of letters. The keys can be remapped to any amount of letters, but each letter must be mapped to exactly one key. You need to find the minimum number of times the keys will be pushed to type the string word.
#
# Return the minimum number of pushes needed to type word after remapping the keys.
#
# An example mapping of letters to keys on a telephone keypad is given below. Note that 1, *, #, and 0 do not map to any letters.


class Solution:
    def minimumPushes(self, word: str) -> int:
        # Frequency array for each letter
        freq = [0] * 26
        for c in word:
            freq[ord(c) - ord('a')] += 1

        # Sort frequencies in descending order
        freq.sort(reverse=True)

        # Find the size of the array without trailing zeroes
        sz = next((i for i, x in enumerate(freq) if x == 0), 26)

        # Calculate the minimum pushes
        total_pushes = 0
        for i in range(sz):
            total_pushes += freq[i] * (i // 8 + 1)

        return total_pushes