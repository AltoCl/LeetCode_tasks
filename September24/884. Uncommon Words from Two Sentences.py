# A sentence is a string of single-space separated words where each word consists only of lowercase letters.
#
# A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
#
# Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # Split the sentences into words
        words_s1 = s1.split()
        words_s2 = s2.split()

        # Combine all words into one list
        all_words = words_s1 + words_s2

        # Count the frequency of each word
        word_count = Counter(all_words)

        # Find words that occur exactly once
        return [word for word in word_count if word_count[word] == 1]