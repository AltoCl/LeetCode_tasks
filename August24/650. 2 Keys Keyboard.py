# There is only one character 'A' on the screen of a notepad. You can perform one of two operations on this notepad for each step:
#
# Copy All: You can copy all the characters present on the screen (a partial copy is not allowed).
# Paste: You can paste the characters which are copied last time.
# Given an integer n, return the minimum number of operations to get the character 'A' exactly n times on the screen.


class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0

        self.target_length = n

        def find_min_steps(current_length: int, clipboard_length: int) -> int:
            if current_length == self.target_length:
                return 0
            if current_length > self.target_length:
                return float('inf')

            copy_and_paste = 2 + find_min_steps(current_length * 2, current_length)
            paste_only = 1 + find_min_steps(current_length + clipboard_length, clipboard_length)

            return min(copy_and_paste, paste_only)

        return 1 + find_min_steps(1, 1)
