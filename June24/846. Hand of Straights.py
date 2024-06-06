# Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.
#
# Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

from collections import Counter
import heapq


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        card_count = Counter(hand)
        min_heap = list(card_count.keys())
        heapq.heapify(min_heap)

        while min_heap:
            first_card = min_heap[0]
            for i in range(first_card, first_card + groupSize):
                if card_count[i] == 0:
                    return False
                card_count[i] -= 1
                if card_count[i] == 0:
                    if i != min_heap[0]:
                        return False
                    heapq.heappop(min_heap)

        return True