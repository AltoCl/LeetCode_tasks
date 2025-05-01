# You have n tasks and m workers. Each task has a strength requirement stored in a 0-indexed integer array tasks, with the ith task requiring tasks[i] strength to complete. The strength of each worker is stored in a 0-indexed integer array workers, with the jth worker having workers[j] strength. Each worker can only be assigned to a single task and must have a strength greater than or equal to the task's strength requirement (i.e., workers[j] >= tasks[i]).
#
# Additionally, you have pills magical pills that will increase a worker's strength by strength. You can decide which workers receive the magical pills, however, you may only give each worker at most one magical pill.
#
# Given the 0-indexed integer arrays tasks and workers and the integers pills and strength, return the maximum number of tasks that can be completed.


from collections import deque

class Solution:
    def maxTaskAssign(self, tasks, workers, pills, strength):
        tasks.sort()
        workers.sort()

        def can_assign(mid):
            boosted = deque()
            w = len(workers) - 1
            free_pills = pills

            for t in reversed(tasks[:mid]):
                if boosted and boosted[0] >= t:
                    boosted.popleft()
                elif w >= 0 and workers[w] >= t:
                    w -= 1
                else:
                    while w >= 0 and workers[w] + strength >= t:
                        boosted.append(workers[w])
                        w -= 1
                    if not boosted or free_pills == 0:
                        return False
                    boosted.pop()
                    free_pills -= 1
            return True

        low, high = 0, min(len(tasks), len(workers))
        while low < high:
            mid = (low + high + 1) // 2
            if can_assign(mid):
                low = mid
            else:
                high = mid - 1
        return low