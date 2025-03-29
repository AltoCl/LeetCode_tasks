# You are given an array nums of n positive integers and an integer k.
#
# Initially, you start with a score of 1. You have to maximize your score by applying the following operation at most k times:
#
# Choose any non-empty subarray nums[l, ..., r] that you haven't chosen previously.
# Choose an element x of nums[l, ..., r] with the highest prime score. If multiple such elements exist, choose the one with the smallest index.
# Multiply your score by x.
# Here, nums[l, ..., r] denotes the subarray of nums starting at index l and ending at the index r, both ends being inclusive.
#
# The prime score of an integer x is equal to the number of distinct prime factors of x. For example, the prime score of 300 is 3 since 300 = 2 * 2 * 3 * 5 * 5.
#
# Return the maximum possible score after applying at most k operations.
#
# Since the answer may be large, return it modulo 109 + 7.


class Solution:
    def countDistinctPrimeFactors(self, n: int) -> int:
        count = 0
        if n % 2 == 0:
            count += 1
            while n % 2 == 0:
                n //= 2

        i = 3
        while i * i <= n:
            if n % i == 0:
                count += 1
                while n % i == 0:
                    n //= i
            i += 2

        if n > 1:
            count += 1
        return count

    def modPow(self, base: int, exp: int, mod: int) -> int:
        result = 1
        b = base % mod
        while exp > 0:
            if exp & 1:
                result = (result * b) % mod
            b = (b * b) % mod
            exp >>= 1
        return result

    def maximumScore(self, nums: List[int], k: int) -> int:
        MOD = 1_000_000_007
        n = len(nums)
        if n == 0:
            return 1

        maxValues = [(-nums[i], i) for i in range(n)]  # Min heap with negative values for max heap behavior
        heapq.heapify(maxValues)

        rightLarge = [n] * n
        leftLarge = [-1] * n
        primeScores = [self.countDistinctPrimeFactors(nums[i]) for i in range(n)]

        stack = []
        for i in range(n):
            while stack and primeScores[i] > primeScores[stack[-1]]:
                rightLarge[stack.pop()] = i
            stack.append(i)

        stack.clear()
        for i in range(n - 1, -1, -1):
            while stack and primeScores[i] >= primeScores[stack[-1]]:
                leftLarge[stack.pop()] = i
            stack.append(i)

        score = 1

        while maxValues and k > 0:
            val, idx = heapq.heappop(maxValues)
            val = -val  # Convert back to positive

            t = (rightLarge[idx] - idx) * (idx - leftLarge[idx])
            steps = min(t, k)

            multiply = self.modPow(val, steps, MOD)
            score = (score * multiply) % MOD

            k -= steps

        return score % MOD