# You are given two arrays of integers, fruits and baskets, each of length n, where fruits[i] represents the quantity of the ith type of fruit, and baskets[j] represents the capacity of the jth basket.
#
# From left to right, place the fruits according to these rules:
#
# Each fruit type must be placed in the leftmost available basket with a capacity greater than or equal to the quantity of that fruit type.
# Each basket can hold only one type of fruit.
# If a fruit type cannot be placed in any basket, it remains unplaced.
# Return the number of fruit types that remain unplaced after all possible allocations are made.


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)
        N = 1
        while N <= n:
            N <<= 1

        segTree = [0] * (2 * N)

        for i in range(n):
            segTree[N + i] = baskets[i]

        for i in range(N - 1, 0, -1):
            segTree[i] = max(segTree[2 * i], segTree[2 * i + 1])

        count = 0
        for fruit in fruits:
            index = 1
            if segTree[index] < fruit:
                count += 1
                continue

            while index < N:
                if segTree[2 * index] >= fruit:
                    index = 2 * index
                else:
                    index = 2 * index + 1

            segTree[index] = -1
            while index > 1:
                index //= 2
                segTree[index] = max(segTree[2 * index], segTree[2 * index + 1])

        return count