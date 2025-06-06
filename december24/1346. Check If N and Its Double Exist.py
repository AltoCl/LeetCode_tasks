# Given an array arr of integers, check if there exist two indices i and j such that :
#
# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:

        seen = set()
        for num in arr:
            if num * 2 in seen or num / 2 in seen:
                return True
            seen.add(num)
        return False
