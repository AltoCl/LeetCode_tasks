# There is a forest with an unknown number of rabbits. We asked n rabbits "How many rabbits have the same color as you?" and collected the answers in an integer array answers where answers[i] is the answer of the ith rabbit.
#
# Given the array answers, return the minimum number of rabbits that could be in the forest.


from collections import Counter
from math import ceil

class Solution:
    def numRabbits(self, answers):
        return sum(ceil(c / (x + 1)) * (x + 1) for x, c in Counter(answers).items())