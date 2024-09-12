# You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.
#
# Return the number of consistent strings in the array words.

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)  # Convert allowed string to a set for O(1) lookups
        consistent_count = 0

        for word in words:
            if all(char in allowed_set for char in word):
                consistent_count += 1

        return consistent_count