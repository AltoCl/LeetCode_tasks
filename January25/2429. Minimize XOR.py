# zGiven two positive integers num1 and num2, find the positive integer x such that:
#
# x has the same number of set bits as num2, and
# The value x XOR num1 is minimal.
# Note that XOR is the bitwise XOR operation.
#
# Return the integer x. The test cases are generated such that x is uniquely determined.
#
# The number of set bits of an integer is the number of 1's in its binary representation.


class Solution(object):
    def minimizeXor(self, num1, num2):
        a, b = bin(num1).count('1'), bin(num2).count('1')
        res = num1
        for i in range(32):
            if a > b and (1 << i) & num1 > 0:
                res ^= 1 << i
                a -= 1
            if a < b and (1 << i) & num1 == 0:
                res ^= 1 << i
                a += 1
        return res