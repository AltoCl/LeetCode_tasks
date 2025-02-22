# Given two strings s and part, perform the following operation on s until all occurrences of the substring part are removed:
#
# Find the leftmost occurrence of the substring part and remove it from s.
# Return s after removing all occurrences of part.
#
# A substring is a contiguous sequence of characters in a string.

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        result_stack = []
        target_length = len(part)
        target_end_char = part[-1]

        for current_char in s:
            result_stack.append(current_char)

            if current_char == target_end_char and len(result_stack) >= target_length:
                if "".join(result_stack[-target_length:]) == part:
                    del result_stack[-target_length:]

        return "".join(result_stack)