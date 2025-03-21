# A happy string is a string that:
#
# consists only of letters of the set ['a', 'b', 'c'].
# s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).
# For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and strings "aa", "baa" and "ababbc" are not happy strings.
#
# Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.
#
# Return the kth string of this list or return an empty string if there are less than k happy strings of length n.

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def dfs(prefix, n, k):
            if n == 0:
                return prefix
            for c in 'abc':
                if prefix and c == prefix[-1]:
                    continue
                cnt = 2 ** (n2 - len(prefix) - 1)
                if cnt >= k:
                    return dfs(prefix + c, n - 1, k)
                else:
                    k -= cnt
            return ""

        n2 = n
        return dfs("", n, k)