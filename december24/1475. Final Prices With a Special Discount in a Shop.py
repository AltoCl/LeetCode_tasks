# You are given an integer array prices where prices[i] is the price of the ith item in a shop.
#
# There is a special discount for items in the shop. If you buy the ith item, then you will receive a discount equivalent to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i]. Otherwise, you will not receive any discount at all.
#
# Return an integer array answer where answer[i] is the final price you will pay for the ith item of the shop, considering the special discount.


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # Create a copy of prices array to store discounted prices
        result = prices.copy()

        stack = deque()

        for i in range(len(prices)):
            # Process items that can be discounted by current price
            while stack and prices[stack[-1]] >= prices[i]:
                # Apply discount to previous item using current price
                result[stack.pop()] -= prices[i]
            # Add current index to stack
            stack.append(i)

        return result
