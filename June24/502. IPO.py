# Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, LeetCode would like to work on some projects to increase its capital before the IPO. Since it has limited resources, it can only finish at most k distinct projects before the IPO. Help LeetCode design the best way to maximize its total capital after finishing at most k distinct projects.
#
# You are given n projects where the ith project has a pure profit profits[i] and a minimum capital of capital[i] is needed to start it.
#
# Initially, you have w capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.
#
# Pick a list of at most k distinct projects from given projects to maximize your final capital, and return the final maximized capital.
#
# The answer is guaranteed to fit in a 32-bit signed integer.

class Solution:
    def findMaximizedCapital(self, numProjects: int, initialCapital: int, profits: List[int], capital: List[int]) -> int:
        projectIndex = 0
        totalProjects = len(profits)

        projects = list(zip(capital, profits))
        projects.sort()

        maxProfitHeap = []

        for currentProject in range(numProjects):
            while projectIndex < totalProjects and projects[projectIndex][0] <= initialCapital:
                heapq.heappush(maxProfitHeap, -projects[projectIndex][1])
                projectIndex += 1

            if not maxProfitHeap:
                return initialCapital

            initialCapital -= heapq.heappop(maxProfitHeap)

        return initialCapital