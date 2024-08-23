# Given a string expression representing an expression of fraction addition and subtraction, return the calculation result in string format.
#
# The final result should be an irreducible fraction. If your final result is an integer, change it to the format of a fraction that has a denominator 1. So in this case, 2 should be converted to 2/1.

from fractions import Fraction
class Solution:
    def fractionAddition(self, expression: str) -> str:
        expression = expression.replace('-', '+-')

        # Split by '+'
        tokens = expression.split('+')

        # Initialize the result
        result = Fraction(0)

        # Iterate through the tokens and sum up the fractions
        for token in tokens:
            if token:  # Make sure it's not an empty string
                result += Fraction(token)

        return (f"{result.numerator}/{result.denominator}")