# Given a sentence that consists of some words separated by a single space, and a searchWord, check if searchWord is a prefix of any word in sentence.
#
# Return the index of the word in sentence (1-indexed) where searchWord is a prefix of this word. If searchWord is a prefix of more than one word, return the index of the first word (minimum index). If there is no such word return -1.
#
# A prefix of a string s is any leading contiguous substring of s.


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        # Split the sentence into words
        words = sentence.split(" ")

        # Iterate over the words
        for i, word in enumerate(words):
            # Check if the word starts with the searchWord
            if word.startswith(searchWord):
                return i + 1  # Return 1-based index

        # Return -1 if no word starts with the searchWord
        return -1