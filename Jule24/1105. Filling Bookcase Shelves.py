# You are given an array books where books[i] = [thicknessi, heighti] indicates the thickness and height of the ith book. You are also given an integer shelfWidth.
#
# We want to place these books in order onto bookcase shelves that have a total width shelfWidth.
#
# We choose some of the books to place on this shelf such that the sum of their thickness is less than or equal to shelfWidth, then build another level of the shelf of the bookcase so that the total height of the bookcase has increased by the maximum height of the books we just put down. We repeat this process until there are no more books to place.
#
# Note that at each step of the above process, the order of the books we place is the same order as the given sequence of books.
#
# For example, if we have an ordered list of 5 books, we might place the first and second book onto the first shelf, the third book on the second shelf, and the fourth and fifth book on the last shelf.
# Return the minimum possible height that the total bookshelf can be after placing shelves in this manner.


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        self.memo = [None] * len(books)
        return self.solve(books, shelfWidth, 0)

    def solve(self, books: List[List[int]], shelfWidth: int, ind: int) -> int:
        if ind == len(books):
            return 0
        if self.memo[ind] is not None:
            return self.memo[ind]

        ans = float('inf')
        maxH = 0
        width = 0
        for i in range(ind, len(books)):
            width += books[i][0]
            if width > shelfWidth:
                break
            maxH = max(maxH, books[i][1])
            ans = min(ans, maxH + self.solve(books, shelfWidth, i + 1))

        self.memo[ind] = ans
        return ans