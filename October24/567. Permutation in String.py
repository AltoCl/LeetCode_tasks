# Given two strings s1 and s2, return true if s2 contains a
# permutation
#  of s1, or false otherwise.
#
# In other words, return true if one of s1's permutations is the substring of s2.

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2=len(s1), len(s2)
        if n2<n1: return False
        freq1, freq2 = Counter(s1), Counter(s2[0:n1])
        if freq1==freq2: return True
        l,  r = 1, n1
        while r<n2:
            freq2[s2[l-1]]-=1
            freq2[s2[r]]+=1
            if freq1==freq2: return True
            r+=1
            l+=1
        return False