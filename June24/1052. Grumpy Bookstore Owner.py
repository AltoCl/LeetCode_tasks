# There is a bookstore owner that has a store open for n minutes. Every minute, some number of customers enter the store. You are given an integer array customers of length n where customers[i] is the number of the customer that enters the store at the start of the ith minute and all those customers leave after the end of that minute.
#
# On some minutes, the bookstore owner is grumpy. You are given a binary array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.
#
# When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise, they are satisfied.
#
# The bookstore owner knows a secret technique to keep themselves not grumpy for minutes consecutive minutes, but can only use it once.
#
# Return the maximum number of customers that can be satisfied throughout the day.

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        i,j =0,0
        k = 0
        sum_ = 0
        max_sum =0
        if len(customers) <= minutes:
            return sum(customers)

        while(j<len(customers)):
            k+=1
            sum_ += 0 if not grumpy[j] else customers[j]
            if k == minutes:
                max_sum = max(max_sum, sum_)
                sum_ -= customers[i] if grumpy[i] else 0
                i+=1
                k-=1
            j+=1
        original_sum = sum([c for i, c in enumerate(customers) if not grumpy[i] ])
        return max_sum + original_sum