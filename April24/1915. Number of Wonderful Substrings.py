# A wonderful string is a string where at most one letter appears an odd number of times.
#
# For example, "ccjjc" and "abab" are wonderful, but "ab" is not.
# Given a string word that consists of the first ten lowercase English letters ('a' through 'j'), return the number of wonderful non-empty substrings in word. If the same substring appears multiple times in word, then count each occurrence separately.
#
# A substring is a contiguous sequence of characters in a string.

class Solution:
  def wonderfulSubstrings(self, word: str) -> int:
    answ = 0
    prefix = 0
    count = [0] * 1024
    count[0] = 1

    for c in word:
      prefix ^= 1 << ord(c) - ord('a')
      answ += count[prefix]
      answ += sum(count[prefix ^ 1 << i] for i in range(10))
      count[prefix] += 1

    return answ