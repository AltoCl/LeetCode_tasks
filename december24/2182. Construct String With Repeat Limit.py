# You are given a string s and an integer repeatLimit. Construct a new string repeatLimitedString using the characters of s such that no letter appears more than repeatLimit times in a row. You do not have to use all characters from s.
#
# Return the lexicographically largest repeatLimitedString possible.
#
# A string a is lexicographically larger than a string b if in the first position where a and b differ, string a has a letter that appears later in the alphabet than the corresponding letter in b. If the first min(a.length, b.length) characters do not differ, then the longer string is the lexicographically larger one.

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        chars = sorted(s, reverse=True)

        result = []
        freq = 1
        pointer = 0

        for i in range(len(chars)):
            if result and result[-1] == chars[i]:
                if freq < repeatLimit:
                    result.append(chars[i])
                    freq += 1
                else:
                    pointer = max(pointer, i + 1)
                    while pointer < len(chars) and chars[pointer] == chars[i]:
                        pointer += 1

                    if pointer < len(chars):
                        result.append(chars[pointer])
                        chars[i], chars[pointer] = chars[pointer], chars[i]
                        freq = 1
                    else:
                        break
            else:
                result.append(chars[i])
                freq = 1

        return ''.join(result)
