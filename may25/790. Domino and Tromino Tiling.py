# You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.

class Solution:
    def numTilings(self, n: int) -> int:
        a=(1,1,2)
        @cache
        def f(n):
            if n<3: return a[n]
            return (2*f(n-1)+f(n-3))%(10**9+7)
        return f(n)