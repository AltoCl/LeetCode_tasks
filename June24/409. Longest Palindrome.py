# Given a string s which consists of lowercase or uppercase letters, return the length of the longest
# palindrome
#  that can be built with those letters.
#
# Letters are case sensitive, for example, "Aa" is not considered a palindrome

class Solution:
    def longestPalindrome(self, s: str) -> int:
            return min(sum(v&~1 for v in Counter(s).values())+1,len(s))