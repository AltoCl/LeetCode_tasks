# Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three. Otherwise, return false.
#
# An integer y is a power of three if there exists an integer x such that y == 3x.

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n>0:
            q, r=divmod(n, 3)
            if r==2: return False
            n=q
        return True