# Given an integer n, return true if it is a power of three. Otherwise, return false.
#
# An integer n is a power of three, if there exists an integer x such that n == 3x.

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        count1 = 0
        while n > 0:
            digit = n % 3
            if digit == 1:
                count1 += 1
            if digit == 2:
                return False
            n //= 3
        return count1 == 1