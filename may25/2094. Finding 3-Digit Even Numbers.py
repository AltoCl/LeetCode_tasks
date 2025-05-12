# You are given an integer array digits, where each element is a digit. The array may contain duplicates.
#
# You need to find all the unique integers that follow the given requirements:
#
# The integer consists of the concatenation of three elements from digits in any arbitrary order.
# The integer does not have leading zeros.
# The integer is even.
# For example, if the given digits were [1, 2, 3], integers 132 and 312 follow the requirements.
#
# Return a sorted array of the unique integers.

class Solution:
    def findEvenNumbers(self, dig: List[int]) -> List[int]:

        arr = []
        for i in range(100, 999):
            flag = True
            seen = Counter(dig)
            for s in str(i):
                if int(s) not in seen:
                    flag = False
                    break
                else:
                    seen[int(s)] -= 1
                    if seen[int(s)] == 0:
                        del seen[int(s)]
            if flag and i % 2 == 0:
                arr.append(i)

        return arr


