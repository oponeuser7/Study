from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        #Title: Maximal Rectangle
        #Approach: DP
        #Why?: You might think of graph search and the condition of a rectangle.
        #But this can't be the apporach. The idea is like this. When there is a
        #row of continuous 1 row itself is a rectangle. And if there is a row of
        #continuos 1 above this row and it is shorter than the below one, these
        #two rows can make a rectangle which has a size of above one and on and
        #on.
        if not matrix: return 0
        ans = 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            acc = 0
            for j in range(n):
                if matrix[i][j]=="1": 
                    acc += 1
                    dp[i][j] = acc
                else:
                    acc = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]=="1":
                    row, col = 1, dp[i][j]
                    for k in range(i, -1, -1):
                        col = min(dp[k][j], col)
                        ans = max(ans, row*col)
                        print("row is ",row," col is ",col)
                        row += 1
        return ans
