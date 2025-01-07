# Given an array of string words, return all strings in words that is a substring of another word. You can return the answer in any order.
#
# A substring is a contiguous sequence of characters within a string


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = set()
        for x in words:
            for y in words:
                if x != y and x in y:
                    ans.add(x)
        return list(ans)