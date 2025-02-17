# You have n  tiles, where each tile has one letter tiles[i] printed on it.
#
# Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        return len(set(p for i in range(1, len(tiles) + 1) for p in permutations(tiles, i)))
