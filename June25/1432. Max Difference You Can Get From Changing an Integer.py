# You are given an integer num. You will apply the following steps to num two separate times:
#
# Pick a digit x (0 <= x <= 9).
# Pick another digit y (0 <= y <= 9). Note y can be equal to x.
# Replace all the occurrences of x in the decimal representation of num by y.
# Let a and b be the two results from applying the operation to num independently.
#
# Return the max difference between a and b.
#
# Note that neither a nor b may have any leading zeros, and must not be 0.


class Solution:
    def maxDiff(self, num: int) -> int:
        numStr = str(num)
        uniqueDigits = set(numStr)
        maxVal = num
        minVal = num

        for digit in uniqueDigits:
            for newDigit in '0123456789':
                if numStr[0] == digit and newDigit == '0':
                    continue
                newNumStr = numStr.replace(digit, newDigit)
                newNum = int(newNumStr)
                maxVal = max(maxVal, newNum)
                minVal = min(minVal, newNum)

        return maxVal - minVal