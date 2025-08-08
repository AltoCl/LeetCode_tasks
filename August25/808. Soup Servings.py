# You have two soups, A and B, each starting with n mL. On every turn, one of the following four serving operations is chosen at random, each with probability 0.25 independent of all previous turns:
#
# pour 100 mL from type A and 0 mL from type B
# pour 75 mL from type A and 25 mL from type B
# pour 50 mL from type A and 50 mL from type B
# pour 25 mL from type A and 75 mL from type B
# Note:
#
# There is no operation that pours 0 mL from A and 100 mL from B.
# The amounts from A and B are poured simultaneously during the turn.
# If an operation asks you to pour more than you have left of a soup, pour all that remains of that soup.
# The process stops immediately after any turn in which one of the soups is used up.
#
# Return the probability that A is used up before B, plus half the probability that both soups are used up in the same turn. Answers within 10-5 of the actual answer will be accepted.


class Solution:
    def soupServings(self, n: int) -> float:
        if n > 50000: return 1.0

        @cache
        def dfs(A, B):
            if A <= 0 and B > 0: return 1
            if A <= 0 and B <= 0: return 0.5
            if A > 0 and B <= 0: return 0
            return 0.25 * (dfs(A - 4, B) + dfs(A - 3, B - 1) + dfs(A - 2, B - 2) + dfs(A - 1, B - 3))

        N = (n + 24) // 25
        return dfs(N, N)
