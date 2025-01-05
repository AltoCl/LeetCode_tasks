# You are given a string s of lowercase English letters and a 2D integer array shifts where shifts[i] = [starti, endi, directioni]. For every i, shift the characters in s from the index starti to the index endi (inclusive) forward if directioni = 1, or shift the characters backward if directioni = 0.
#
# Shifting a character forward means replacing it with the next letter in the alphabet (wrapping around so that 'z' becomes 'a'). Similarly, shifting a character backward means replacing it with the previous letter in the alphabet (wrapping around so that 'a' becomes 'z').
#
# Return the final string after all such shifts to s are applied.


class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        n = len(s)
        shift = [0] * (n + 1)

        for shiftOp in shifts:
            start, end, direction = shiftOp
            shift[start] += (1 if direction == 1 else -1)
            if end + 1 < n:
                shift[end + 1] -= (1 if direction == 1 else -1)

        currentShift = 0
        shiftList = list(s)
        for i in range(n):
            currentShift += shift[i]
            netShift = (currentShift % 26 + 26) % 26
            shiftList[i] = chr((ord(shiftList[i]) - ord('a') + netShift) % 26 + ord('a'))

        return ''.join(shiftList)