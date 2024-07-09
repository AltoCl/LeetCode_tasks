# There is a restaurant with a single chef. You are given an array customers, where customers[i] = [arrivali, timei]:
#
# arrivali is the arrival time of the ith customer. The arrival times are sorted in non-decreasing order.
# timei is the time needed to prepare the order of the ith customer.
# When a customer arrives, he gives the chef his order, and the chef starts preparing it once he is idle. The customer waits till the chef finishes preparing his order. The chef does not prepare food for more than one customer at a time. The chef prepares food for customers in the order they were given in the input.
#
# Return the average waiting time of all customers. Solutions within 10-5 from the actual answer are considered accepted.
#
class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        n: int = len(customers)
        time_waiting: int = customers[0][1]
        finished_prev = customers[0][0] + customers[0][1]

        for customer_ind in range(1, n, 1):
            times: list[int] = customers[customer_ind]
            arrive: int = times[0]

            # chef starts cook this as soon as he finished last dish or customer arrived
            start_cook: int = max(arrive, finished_prev)
            end_time: int = start_cook + times[1]
            finished_prev: int = end_time
            time_waiting += end_time - arrive

        return time_waiting / n