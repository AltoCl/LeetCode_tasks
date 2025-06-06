# You are given a string s and a robot that currently holds an empty string t. Apply one of the following operations until s and t are both empty:
#
# Remove the first character of a string s and give it to the robot. The robot will append this character to the string t.
# Remove the last character of a string t and give it to the robot. The robot will write this character on paper.
# Return the lexicographically smallest string that can be written on the paper.



class Solution:
    def robotWithString(self, s: str) -> str:
        from collections import Counter

        freq = Counter(s)
        stack = []
        result = []
        a_ord = ord('a')

        def has_smaller(top):
            for i in range(top):
                if freq[chr(i + a_ord)] > 0:
                    return True
            return False

        for ch in s:
            freq[ch] -= 1
            stack.append(ch)
            while stack and not has_smaller(ord(stack[-1]) - a_ord):
                result.append(stack.pop())

        return ''.join(result)