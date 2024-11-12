# You are given a 2D integer array items where items[i] = [pricei, beautyi] denotes the price and beauty of an item respectively.
#
# You are also given a 0-indexed integer array queries. For each queries[j], you want to determine the maximum beauty of an item whose price is less than or equal to queries[j]. If no such item exists, then the answer to this query is 0.
#
# Return an array answer of the same length as queries where answer[j] is the answer to the jth query.


class Solution(object):
    def maximumBeauty(self, items, queries):

        maxI = float('inf')
        res = [[0, 0, maxI]]

        items.sort(key=lambda x: x[0])

        for price, beauty in items:
            lastBracket = res[-1]
            if beauty > lastBracket[1]:
                res[-1][2] = price
                res.append([price, beauty, maxI])

        ans = []

        for x in queries:
            for i in range(len(res) - 1, -1, -1):
                if res[i][0] <= x:
                    ans.append(res[i][1])
                    break

        return ans