#Given a 0-indexed string word and a character ch,
# reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive).
# If the character ch does not exist in word, do nothing.

#For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at 3 (inclusive).
# The resulting string will be "dcbaefd".


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        subs_to_reverse = ""
        subs = ""
        flag = 0
        for s in word:
            subs += s
            if s == ch and flag == 0:
                subs_to_reverse = subs[::-1]
                subs = ""
                flag = 999
        return subs_to_reverse + subs
