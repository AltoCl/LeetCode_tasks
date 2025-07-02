# You are given an integer array nums.
#
# In one move, you can choose one element of nums and change it to any value.
#
# Return the minimum difference between the largest and smallest value of nums after performing at most three moves.
#
class Solution:
    def minDifference(self, a: List[int]) -> int:
        return min(map(sub,nlargest(4,a)[::-1],nsmallest(4,a)))