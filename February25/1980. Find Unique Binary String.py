#Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.


class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        res=[]
        for i in range(0, len(nums)):
            if nums[i][i]=='0':
                res.append('1')
            else:
                res.append('0')

        return "".join(res)