# Given a string s, return the number of unique palindromes of length three that are a subsequence of s.
#
# Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.
#
# A palindrome is a string that reads the same forwards and backwards.
#
# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
#
# For example, "ace" is a subsequence of "abcde".


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        R = [0] * 26
        for u in s:
            R[ord(u) - ord('a')] += 1

        L = [0] * 26
        S = set()

        for i in range(len(s)):
            t = ord(s[i]) - ord('a')
            R[t] -= 1
            for j in range(26):
                if L[j] > 0 and R[j] > 0:
                    S.add(26 * t + j)
            L[t] += 1

        return len(S)