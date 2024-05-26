# An attendance record for a student can be represented as a string where each character signifies whether the student was
# absent, late, or present on that day. The record only contains the following three characters:
class Solution:
    def checkRecord(self, n: int) -> int:
        md = 1000000007
        dp = [1, 0, 0, 0, 0, 0]
        for i in range(n):
            d0, d1, d2, d3, d4, _ = dp

            dp = list(map(lambda x: x % md,
                          [d0 + d1 + d2, d0, d1,
                           sum(dp), d3, d4]))

        return sum(dp) % md