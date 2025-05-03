# In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)
#
# We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.
#
# Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.
#
# If it cannot be done, return -1.


class Solution:
    def minDominoRotations(self, tops, bottoms):
        res = float('inf')
        for val in range(1, 7):
            top_swaps = bottom_swaps = 0
            valid = True
            for t, b in zip(tops, bottoms):
                if t != val and b != val:
                    valid = False
                    break
                if t != val:
                    top_swaps += 1
                if b != val:
                    bottom_swaps += 1
            if valid:
                res = min(res, top_swaps, bottom_swaps)
        return -1 if res == float('inf') else res