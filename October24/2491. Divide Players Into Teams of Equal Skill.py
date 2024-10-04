# You are given a positive integer array skill of even length n where skill[i] denotes the skill of the ith player. Divide the players into n / 2 teams of size 2 such that the total skill of each team is equal.
#
# The chemistry of a team is equal to the product of the skills of the players on that team.
#
# Return the sum of the chemistry of all the teams, or return -1 if there is no way to divide the players into teams such that the total skill of each team is equal.


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # Step 1: Sort the skill array
        skill.sort()

        total_skill = skill[0] + skill[-1]  # Required sum for each pair
        chemistry_sum = 0

        # Step 2: Pair players using two pointers
        for i in range(len(skill) // 2):
            # Check if the sum of current pair matches the required total_skill
            if skill[i] + skill[-i - 1] != total_skill:
                return -1  # Invalid configuration, return -1
            # Calculate the chemistry (product of pair) and add it to the sum
            chemistry_sum += skill[i] * skill[-i - 1]

        return chemistry_sum  # Return total chemistry