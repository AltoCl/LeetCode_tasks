# You are given a string s consisting of lowercase English letters.
#
# Your task is to find the maximum difference diff = freq(a1) - freq(a2) between the frequency of characters a1 and a2 in the string such that:
#
# a1 has an odd frequency in the string.
# a2 has an even frequency in the string.
# Return this maximum difference.

class Solution:
    def maxDifference(self, s: str) -> int:
        s = sorted(s)

        mx_odd = 0
        min_even = float('inf')

        cur = s[0]
        cnt = 1

        for i in range(1, len(s)):
            if s[i] == cur:
                cnt += 1
            else:
                if cnt % 2 == 1:
                    mx_odd = max(mx_odd, cnt)
                else:
                    min_even = min(min_even, cnt)
                cur = s[i]
                cnt = 1

        # Last group handling
        if cnt % 2 == 1:
            mx_odd = max(mx_odd, cnt)
        else:
            min_even = min(min_even, cnt)

        return mx_odd - min_even