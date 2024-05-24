# Given a list of words, list of  single letters (might be repeating) and score of every character.
#
# Return the maximum score of any valid set of words formed by using the given letters (words[i] cannot be used two or more times).
#
# It is not necessary to use all characters in letters and each letter can only be used once. Score of letters 'a', 'b', 'c', ... ,'z' is given by score[0], score[1], ... , score[25] respectively.

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        n = len(words)
        m = 1 << n
        inf = 1 << 31
        letterCounter = {i:0 for i in range(26)}
        for ch in letters:
            idx = ord(ch) - ord('a')
            letterCounter[idx] += 1
        def CountFreq(s, letterCounter):
            ans = 0
            for c in s:
                if letterCounter[ord(c) - ord('a')] == 0:
                    return -inf
                ans += score[ord(c) - ord('a')]
                letterCounter[ord(c) - ord('a')] -= 1
            return ans
        maxScore = -inf
        for i in range(m):
            Score = 0
            tmp = letterCounter.copy()
            for j in range(n):
                # If the word is part of subset
                if i & (1<< j):
                    curr_Score = CountFreq(words[j], tmp)
                    if curr_Score == -inf:
                        Score = -inf
                    else:
                        Score += curr_Score
            if Score > maxScore:
                maxScore = Score
        return maxScore