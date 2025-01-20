# You are given a 0-indexed integer array arr, and an m x n integer matrix mat. arr and mat both contain all the integers in the range [1, m * n].
#
# Go through each index i in arr starting from index 0 and paint the cell in mat containing the integer arr[i].
#
# Return the smallest index i at which either a row or a column will be completely painted in mat.

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n=len(mat), len(mat[0])
        N=m*n

        to_i=[-1]*(N+1)
        to_j=[-1]*(N+1)
        for i, row in enumerate(mat):
            for j, x in enumerate(row):
                to_i[x]=i
                to_j[x]=j
        R=[0]*m
        C=[0]*n
        for i, x in enumerate(arr):
            R[to_i[x]]+=1
            C[to_j[x]]+=1
            if R[to_i[x]]==n or C[to_j[x]]==m:
                return i
        return -1