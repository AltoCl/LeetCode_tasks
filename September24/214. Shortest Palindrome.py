# You are given a string s. You can convert s to a
# palindrome
#  by adding characters in front of it.

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        r = s[::-1]
        for i in range(len(s)+1):
            if s.startswith(r[i:]):
                return r[:i] + s