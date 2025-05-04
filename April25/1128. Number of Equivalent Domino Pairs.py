# Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a == c and b == d), or (a == d and b == c) - that is, one domino can be rotated to be equal to another domino.
#
# Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        freq = [0] * 100
        cnt = 0
        for d0, d1 in dominoes:
            x = 10 * d0 + d1 if d0 < d1 else 10 * d1 + d0
            cnt += freq[x]
            freq[x] += 1
        return cnt
