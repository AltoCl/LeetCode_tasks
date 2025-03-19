# You are given a binary array nums.
#
# You can do the following operation on the array any number of times (possibly zero):
#
# Choose any 3 consecutive elements from the array and flip all of them.
# Flipping an element means changing its value from 0 to 1, and from 1 to 0.
#
# Return the minimum number of operations required to make all elements in nums equal to 1. If it is impossible, return -1.

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n, i0, op = len(nums), -1, 0
        nums.append(0)  # append 0 avoid of try-except
        while True:
            i0 = nums.index(0, i0 + 1)  # Find next 0
            if i0 >= n - 2:
                break
            nums[i0 + 1] ^= 1  # Use xor to flip i0+1
            nums[i0 + 2] ^= 1  # Flip i0+2
            op += 1
        return op if i0 >= n else -1
