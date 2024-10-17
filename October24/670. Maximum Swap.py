# You are given an integer num. You can swap two digits at most once to get the maximum valued number.
#
# Return the maximum valued number you can get.


class Solution:
    def maximumSwap(self, nums: int) -> int:
        nums = list(str(nums))
        a = []
        for i in nums:
            a.append((-1) * int(i))
        a.sort() #in order to find the maximum number/ alternative version of heap
        for j in range(len(nums)):
            if int(nums[j]) != (-1) * a[0]: #the case where we need to do swap
                index = len(nums) - 1 - nums[::-1].index(str((-1) * a[0]))
                print(index)
                print(nums[::-1])
                nums[j], nums[index] = nums[index], nums[j]
                break
            else:
                a.pop(0) #in other cases where we do not need to swap any letters as the maximum digits stay on their places
        return int(''.join(nums))