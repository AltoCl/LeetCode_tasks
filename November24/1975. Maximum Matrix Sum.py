# You are given an n x n integer matrix. You can do the following operation any number of times:
#
# Choose any two adjacent elements of matrix and multiply each of them by -1.
# Two elements are considered adjacent if and only if they share a border.
#
# Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of the matrix's elements using the operation mentioned above.


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total_sum = 0
        negative_count = 0
        min_abs_value = float('inf')

        for row in matrix:
            for value in row:
                total_sum += abs(value)
                if value < 0:
                    negative_count += 1
                min_abs_value = min(min_abs_value, abs(value))

        # If the count of negative numbers is odd, subtract twice the smallest absolute value
        if negative_count % 2 == 1:
            total_sum -= 2 * min_abs_value

        return total_sum