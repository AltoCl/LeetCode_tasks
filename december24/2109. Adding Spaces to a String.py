# You are given a 0-indexed string s and a 0-indexed integer array spaces that describes the indices in the original string where spaces will be added. Each space should be inserted before the character at the given index.
#
# For example, given s = "EnjoyYourCoffee" and spaces = [5, 9], we place spaces before 'Y' and 'C', which are at indices 5 and 9 respectively. Thus, we obtain "Enjoy Your Coffee".
# Return the modified string after the spaces have been added.

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        m, n=len(spaces), len(s)
        t=[' ']*(m+n)
        j=0
        for i, c in enumerate(s):
            if j<m and i==spaces[j]:
                j+=1
            t[i+j]=s[i]
        return "".join(t)