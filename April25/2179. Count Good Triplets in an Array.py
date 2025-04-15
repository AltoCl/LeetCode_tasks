# You are given two 0-indexed arrays nums1 and nums2 of length n, both of which are permutations of [0, 1, ..., n - 1].
#
# A good triplet is a set of 3 distinct values which are present in increasing order by position both in nums1 and nums2. In other words, if we consider pos1v as the index of the value v in nums1 and pos2v as the index of the value v in nums2, then a good triplet will be a set (x, y, z) where 0 <= x, y, z <= n - 1, such that pos1x < pos1y < pos1z and pos2x < pos2y < pos2z.
#
# Return the total number of good triplets.

class Solution:
    def goodTriplets(self, nums1, nums2):
        n = len(nums1)
        pos2 = {nums2[i]: i for i in range(n)}

        # Map nums1[i] to its position in nums2
        mapped = [pos2[nums1[i]] for i in range(n)]

        bitLeft = BIT(n)
        bitRight = BIT(n)
        rightCount = [0] * n

        # Count right side first
        for i in range(n - 1, -1, -1):
            rightCount[i] = bitRight.query(n - 1) - bitRight.query(mapped[i])
            bitRight.update(mapped[i], 1)

        result = 0

        # Count left and calculate triplets
        for i in range(n):
            left = bitLeft.query(mapped[i] - 1)
            right = rightCount[i]
            result += left * right
            bitLeft.update(mapped[i], 1)

        return result


class BIT:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 2)

    def update(self, index, delta):
        index += 1
        while index <= self.size + 1:
            self.tree[index] += delta
            index += index & -index

    def query(self, index):
        result = 0
        index += 1
        while index > 0:
            result += self.tree[index]
            index -= index & -index
        return result