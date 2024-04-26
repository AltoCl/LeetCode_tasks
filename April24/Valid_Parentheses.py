# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

class Solution:
    def isValid(self, s: str) -> bool:
        list_of_parenthesses = []
        brackets_dict = {')': '(', '}': '{', ']': '['}
        for symbol in s:
            if symbol in brackets_dict.values():
                list_of_parenthesses.append(symbol)
            elif symbol in brackets_dict.keys():
                if not list_of_parenthesses or brackets_dict[symbol] != list_of_parenthesses.pop():
                    return False
            else:
                return False
        return not list_of_parenthesses