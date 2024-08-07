# Convert a non-negative integer num to its English words representation.


class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        # Helper arrays to convert numbers to words
        less_than_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
                        "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen",
                        "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]

        def helper(n):
            if n == 0:
                return ""
            elif n < 20:
                return less_than_20[n] + " "
            elif n < 100:
                return tens[n // 10] + " " + helper(n % 10)
            else:
                return less_than_20[n // 100] + " Hundred " + helper(n % 100)

        res = ""
        for i, unit in enumerate(thousands):
            if num % 1000 != 0:
                res = helper(num % 1000) + unit + " " + res
            num //= 1000

        return res.strip()