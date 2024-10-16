# A string s is called happy if it satisfies the following conditions:
#
# s only contains the letters 'a', 'b', and 'c'.
# s does not contain any of "aaa", "bbb", or "ccc" as a substring.
# s contains at most a occurrences of the letter 'a'.
# s contains at most b occurrences of the letter 'b'.
# s contains at most c occurrences of the letter 'c'.
# Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".
#
# A substring is a contiguous sequence of characters within a string

import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # Max heap to always pick the character with the highest count.
        pq = []
        if a > 0:
            heapq.heappush(pq, (-a, 'a'))
        if b > 0:
            heapq.heappush(pq, (-b, 'b'))
        if c > 0:
            heapq.heappush(pq, (-c, 'c'))

        result = []

        while pq:
            count1, char1 = heapq.heappop(pq)

            # If the last two characters are the same as char1.
            if len(result) >= 2 and result[-1] == char1 and result[-2] == char1:
                if not pq:
                    break  # No valid characters left to pick.

                count2, char2 = heapq.heappop(pq)
                result.append(char2)
                count2 += 1  # Decrease count (negated)

                if count2 < 0:
                    heapq.heappush(pq, (count2, char2))

                heapq.heappush(pq, (count1, char1))
            else:
                result.append(char1)
                count1 += 1  # Decrease count (negated)

                if count1 < 0:
                    heapq.heappush(pq, (count1, char1))

        return ''.join(result)