# Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).
#
# The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.

class Solution:
    def maxScore(self, s: str) -> int:
        total_zeros = s.count('0')
        ans, zeros, n = -1, 0, len(s)
        for i in range(1, n):
            if s[i - 1] == '0':
                zeros += 1
                total_zeros -= 1
            ans = max(ans, zeros + (n - total_zeros - i))
        return ans
