# There are n soldiers standing in a line. Each soldier is assigned a unique rating value.
#
# You have to form a team of 3 soldiers amongst them under the following rules:
#
# Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
# A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
# Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

# Version B:  O(n^2) solution with (primitive) nested loops for building our 4 counting variables.
class Solution:
    def numTeams(self, A):
        L = len(A)
        result = 0
        for j in range(1,L-1):
            x, lo_L, lo_R, hi_L, hi_R = A[j], 0, 0, 0, 0
            for i in range(j):
                if A[i]<x:
                    lo_L += 1
                else:
                    hi_L += 1
            for k in range(j+1,L):
                if A[k]<x:
                    lo_R += 1
                else:
                    hi_R += 1
            result += lo_L*hi_R + hi_L*lo_R
        return result