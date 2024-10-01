# Given an array of integers arr of even length n and an integer k.
#
# We want to divide the array into exactly n / 2 pairs such that the sum of each pair is divisible by k.
#
# Return true If you can find a way to do that or false otherwise.


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        freq = [0] * k

        for num in arr:
            remainder = (num % k + k) % k
            freq[remainder] += 1

        if freq[0] % 2 != 0:
            return False

        for i in range(1, k // 2 + 1):
            if freq[i] != freq[k - i]:
                return False

        return True