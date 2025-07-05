# Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.
#
# Return the largest lucky integer in the array. If there is no lucky integer return -1.

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        return max((x for x, f in Counter(arr).items() if x == f), default=-1)
