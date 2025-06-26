# You are given a binary string s and a positive integer k.
#
# Return the length of the longest subsequence of s that makes up a binary number less than or equal to k.
#
# Note:
#
# The subsequence can contain leading zeroes.
# The empty string is considered to be equal to 0.
# A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.


class Solution:
    def numberOfArrays(self, diff: List[int], lower: int, upper: int) -> int:
        return (K := list(accumulate(diff, initial=0))) and max(0, upper - lower + 1 - max(K) + min(K))
