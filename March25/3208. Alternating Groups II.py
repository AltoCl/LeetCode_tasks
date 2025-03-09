# There is a circle of red and blue tiles. You are given an array of integers colors and an integer k. The color of tile i is represented by colors[i]:
#
# colors[i] == 0 means that tile i is red.
# colors[i] == 1 means that tile i is blue.
# An alternating group is every k contiguous tiles in the circle with alternating colors (each tile in the group except the first and last one has a different color from its left and right tiles).
#
# Return the number of alternating groups.
#
# Note that since colors represents a circle, the first and the last tiles are considered to be next to each other.


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        sz = n + k - 1
        ans, alt, prev = 0, 1, colors[0]
        for i in range(1, sz):
            i0 = i % n
            alt = 1 if prev == colors[i0] else alt + 1
            ans += (alt >= k)
            prev = colors[i0]
        return ans
