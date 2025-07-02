# You are given two arrays rowSum and colSum of non-negative integers where rowSum[i] is the sum of the elements in the ith row and colSum[j] is the sum of the elements of the jth column of a 2D matrix. In other words, you do not know the elements of the matrix, but you do know the sums of each row and column.
# Find any matrix of non-negative integers of size rowSum.length x colSum.length that satisfies the rowSum and colSum requirements.
# Return a 2D array representing any matrix that fulfills the requirements. It's guaranteed that at least one matrix that fulfills the requirements exists.
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m = len(rowSum)
        n = len(colSum)

        result = [[0 for j in range(n)] for i in range(m)]

        i = j = 0

        while ( i < m and j < n ):
            result[i][j] = min(rowSum[i],colSum[j])

            rowSum[i] -= result[i][j]
            colSum[j] -= result[i][j]

            if rowSum[i]== 0:
                i+=1

            if colSum[j]==0:
                j+=1

        return result
