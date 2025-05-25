# You are given an array of strings words. Each element of words consists of two lowercase English letters.
#
# Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.
#
# Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.
#
# A palindrome is a string that reads the same forward and backward.

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        freq=Counter(words)
        pal=0
        hasDouble=False
        for key, val in freq.items():
            if key[0]==key[1]:
                pal+=val//2*4
                if val&1: hasDouble=True
            elif key[0]<key[1]:
                rev=key[1]+key[0]
                pal+=min(val, freq[rev] )*4
        return pal+hasDouble*2