# You are given a 0-indexed array of positive integers nums.
#
# In one operation, you can swap any two adjacent elements if they have the same number of
# set bits
# . You are allowed to do this operation any number of times (including zero).
#
# Return true if you can sort the array, else return false.


class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        pmax = cmin = cmax = pcnt = 0
        for v in nums:
            ccnt = v.bit_count()
            if pcnt == ccnt:
                cmin = min(cmin, v)
                cmax = max(cmax, v)
            elif cmin < pmax:
                return False
            else:
                pmax = cmax
                cmin = cmax = v
                pcnt = ccnt
        return cmin >= pmax