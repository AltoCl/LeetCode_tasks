# Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.
#
# Note that the same word in the dictionary may be reused multiple times in the segmentation.

class Solution:
    def wordBreak(self, s: str, w: List[str]) -> bool:
        def f(i):
            result = [s[i:]] if s[i:] in w else []
            for j in range(i+1, len(s)):
                if s[i:j] in w:
                    for t in f(j):
                        result.append(s[i:j]+' '+t)

            return result

        return f(0)