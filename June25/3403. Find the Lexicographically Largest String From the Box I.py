# You are given a string word, and an integer numFriends.
#
# Alice is organizing a game for her numFriends friends. There are multiple rounds in the game, where in each round:
#
# word is split into numFriends non-empty strings, such that no previous round has had the exact same split.
# All the split words are put into a box.
# Find the lexicographically largest string from the box after all the rounds are finished.

class Solution:
    def answerString(self, word: str, n: int) -> str:
        m=len(word)-n+1 # splits to be done with m length
        if n==1: # if only one split we can do total word is taken
            return word
# else check all m length splits and gind max in them
        return max(word[i:i+m] for i in range(len(word)))