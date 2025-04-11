# You are given two positive integers low and high.
#
# An integer x consisting of 2 * n digits is symmetric if the sum of the first n digits of x is equal to the sum of the last n digits of x. Numbers with an odd number of digits are never symmetric.
#
# Return the number of symmetric integers in the range [low, high].

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0  # 🍜 Mission count

        for num in range(low, high + 1):
            s = str(num)  # 🔍 Naruto's string transformation no jutsu
            n = len(s)

            if n % 2 != 0:
                continue  # ☠️ Odd-digit numbers are not balanced, skip

            half = n // 2
            left = sum(int(s[i]) for i in range(half))  # ⬅️ Left chakra
            right = sum(int(s[i]) for i in range(half, n))  # ➡️ Right chakra

            if left == right:
                count += 1  # ✅ Symmetry detected, add to mission count

        return count