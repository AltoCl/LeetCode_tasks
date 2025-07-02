# You are given a string s that consists of lower case English letters and brackets.
#
# Reverse the strings in each pair of matching parentheses, starting from the innermost one.
#
# Your result should not contain any brackets.

class Solution:
    def reverseParentheses(self, s: str) -> str:
        ind_stack: deque[int] = deque()
        res: list[str] = []

        for char in s:
            if char == "(":  # start new string we need to reverse first
                ind_stack.append(len(res))  # string starts on next index
            elif char == ")":  # reverse string from last added start index
                start_ind: int = ind_stack.pop()
                res[start_ind:] = res[start_ind:][::-1]
            else:
                res.append(char)

        return "".join(res)