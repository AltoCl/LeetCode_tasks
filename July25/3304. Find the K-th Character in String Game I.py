# Alice and Bob are playing a game. Initially, Alice has a string word = "a".
#
# You are given a positive integer k.
#
# Now Bob will ask Alice to perform the following operation forever:
#
# Generate a new string by changing each character in word to its next character in the English alphabet, and append it to the original word.
# For example, performing the operation on "c" generates "cd" and performing the operation on "zb" generates "zbac".
#
# Return the value of the kth character in word, after enough operations have been done for word to have at least k characters.
#
# Note that the character 'z' can be changed to 'a' in the operation.


def findKthCharacter(self, k: int):
    # convert the 1-based 'k' to a 0-based index
    index = k - 1

    # calculate the number of set bits
    # this will be the total number of times the character has been incremented
    increments = 0

    while index > 0:
        # find the largest power of 2 less than or equal to the current index
        # this represents the length of the string before the current char was generated
        p = 1
        while p * 2 <= index:
            p *= 2

        # since we must subtract p to find the parent index, it means our character
        # was in the second half of the string generation
        # so, we count an increment
        increments += 1

        # subtract the largest power of two from the index
        index -= p

    # calculate the final character
    # start with the ASCII value of 'a' and add the number of increments
    # use the modulo to handle the wrap-around from 'z' to 'a'
    final_char_code = ord('a') + (increments % 26)

    return chr(final_char_code)