import math

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[1 for i in range(n)] for j in range(n)]
        cur = 0
        cycle = n//2 if n%2==0 else (n//2)+1
        for i in range(cycle):
            for j in range(i, n-1-i):
                cur += 1
                ans[0+i][j] = cur
            for j in range(i, n-1-i):
                cur += 1
                ans[j][n-1-i] = cur
            for j in range(n-1-i, i, -1):
                cur += 1
                ans[n-1-i][j] = cur
            for j in range(n-1-i, i, -1):
                cur += 1
                ans[j][0+i] = cur
        if n%2!=0: ans[n//2][n//2] = cur+1
        return ans
