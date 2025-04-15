# You are given two 0-indexed arrays nums1 and nums2 of length n, both of which are permutations of [0, 1, ..., n - 1].
#
# A good triplet is a set of 3 distinct values which are present in increasing order by position both in nums1 and nums2. In other words, if we consider pos1v as the index of the value v in nums1 and pos2v as the index of the value v in nums2, then a good triplet will be a set (x, y, z) where 0 <= x, y, z <= n - 1, such that pos1x < pos1y < pos1z and pos2x < pos2y < pos2z.
#
# Return the total number of good triplets.

class Solution:
    def goodTriplets(self, nums1, nums2):
        result = self.all_common_subsequences(nums1, nums2)
        return len(self.extract_triplets(result))

    def all_common_subsequences(self, nums1, nums2):
        memo = {}

        def dp(i, j):
            key = f"{i}|{j}"
            if key in memo:
                return memo[key]

            result = set()

            if i >= len(nums1) or j >= len(nums2):
                result.add(())
            else:
                if nums1[i] == nums2[j]:
                    for subseq in dp(i + 1, j + 1):
                        result.add((nums1[i],) + subseq)

                for subseq in dp(i + 1, j):
                    result.add(subseq)
                for subseq in dp(i, j + 1):
                    result.add(subseq)

            memo[key] = result
            return result

        all_subsequences = dp(0, 0)
        return [list(seq) for seq in all_subsequences if len(seq) > 2]

    def extract_triplets(self, subsequences):
        triplets = set()

        for subseq in subsequences:
            n = len(subseq)
            for i in range(n - 2):
                for j in range(i + 1, n - 1):
                    for k in range(j + 1, n):
                        triplet = (subseq[i], subseq[j], subseq[k])
                        triplets.add(triplet)

        return {list(triplet) for triplet in triplets}