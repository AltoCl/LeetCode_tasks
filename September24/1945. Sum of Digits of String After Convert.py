# You are given a string s consisting of lowercase English letters, and an integer k.
#
# First, convert s into an integer by replacing each letter with its position in the alphabet (i.e., replace 'a' with 1, 'b' with 2, ..., 'z' with 26). Then, transform the integer by replacing it with the sum of its digits. Repeat the transform operation k times in total.
#
# For example, if s = "zbax" and k = 2, then the resulting integer would be 8 by the following operations:
#
# Convert: "zbax" ➝ "(26)(2)(1)(24)" ➝ "262124" ➝ 262124
# Transform #1: 262124 ➝ 2 + 6 + 2 + 1 + 2 + 4 ➝ 17
# Transform #2: 17 ➝ 1 + 7 ➝ 8
# Return the resulting integer after performing the operations described above.


class Solution(object):
    def getLucky(self, s, k):
        # Convert each character in the string to its corresponding numeric value
        number = ''
        for x in s:
            number += str(ord(x) - ord('a') + 1)

        # Perform the transformation `k` times
        while k > 0:
            temp = 0
            for x in number:
                temp += int(x)  # Sum the digits of the current number
            number = str(temp)  # Convert the sum back to a string
            k -= 1
        return int(number)  # Return the final result as an integer