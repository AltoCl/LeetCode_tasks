# Given a string array words, return an array of all characters that show up in all strings within the words
# (including duplicates). You may return the answer in any order.

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common_counter = Counter(words[0])

        for word in words[1:]:
            word_counter = Counter(word)
            for char in common_counter:
                common_counter[char] = min(common_counter[char], word_counter[char])

        result = []
        for char, freq in common_counter.items():
            result.extend([char] * freq)

        return result