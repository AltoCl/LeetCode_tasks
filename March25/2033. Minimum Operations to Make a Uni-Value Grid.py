# You are given a 2D integer grid of size m x n and an integer x. In one operation, you can add x to or subtract x from any element in the grid.
#
# A uni-value grid is a grid where all the elements of it are equal.
#
# Return the minimum number of operations to make the grid uni-value. If it is not possible, return -1.

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = [num for row in grid for num in row]  # Flatten the grid
        arr.sort()
        median = arr[len(arr) // 2]  # Find the median

        # Check if all elements can be transformed
        for num in arr:
            if (num - median) % x != 0:
                return -1  # Impossible case

        # Calculate the minimum number of operations
        return sum(abs(num - median) // x for num in arr)