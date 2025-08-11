# Given a positive integer n, there exists a 0-indexed array called powers, composed of the minimum number of powers of 2 that sum to n. The array is sorted in non-decreasing order, and there is only one way to form the array.
#
# You are also given a 0-indexed 2D integer array queries, where queries[i] = [lefti, righti]. Each queries[i] represents a query where you have to find the product of all powers[j] with lefti <= j <= righti.
#
# Return an array answers, equal in length to queries, where answers[i] is the answer to the ith query. Since the answer to the ith query may be too large, each answers[i] should be returned modulo 109 + 7.


class Solution:
    def productQueries(self, num: int, queries: List[List[int]]) -> List[int]:
        powers = []
        while num:
            lowBit = num & -num
            powers.append(lowBit)
            num ^= lowBit

        size = len(powers)
        table = [[0] * size for _ in range(size)]
        for row, val in enumerate(powers):
            table[row][row] = val
            for col in range(row + 1, size):
                table[row][col] = (
                        table[row][col - 1] * powers[col] % (10 ** 9 + 7)
                )

        return [table[p][q] for p, q in queries]
