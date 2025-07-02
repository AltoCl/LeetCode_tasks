# You are given a 0-indexed integer array mapping which represents the mapping rule of a shuffled decimal system. mapping[i] = j means digit i should be mapped to digit j in this system.
#
# The mapped value of an integer is the new integer obtained by replacing each occurrence of digit i in the integer with mapping[i] for all 0 <= i <= 9.
#
# You are also given another integer array nums. Return the array nums sorted in non-decreasing order based on the mapped values of its elements.
#
# Notes:
#
# Elements with the same mapped values should appear in the same relative order as in the input.
# The elements of nums should only be sorted based on their mapped values and not be replaced by them.


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:

        def mapInt(n):
            if not n:
                return mapping[0]
            res, pos = 0, 1
            while n:
                res += mapping[n % 10] * pos
                pos *= 10
                n //= 10
            return res

        # Creates a dictionary with n as the key and a tuple in the form (mapped_value, index)
        pairs = {n: (mapInt(n), idx) for idx, n in enumerate(nums)}

        return sorted(nums, key=lambda x: pairs[x])  # Our key for sorting is the tuple returned by the pairs dictionary