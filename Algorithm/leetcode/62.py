class Solution:
    #there are two solutions for this problem. The first one is DP. You can find out that at a cell(x,y),
    #count of uniquePaths is the sum of count from cell(x+1,y) and cell(x,y+1).
    #The next approach is combination. In this problem, robot can only go right or down. Which means no matter
    #which way robot decides to go, it can be represented as the combination of "R"(go right) and "D"(go down).
    #It is a nCr problem. nCr is n!/(n-r)!r!.
    def uniquePaths_dp(self, m: int, n: int) -> int:
        dp=[[1 for i in range(n)] for j in range(m)]
        for i in range(m-2, -1 ,-1):
            for j in range(n-2, -1, -1):
                dp[i][j] = dp[i+1][j] + dp[i][j+1]
        return dp[0][0]

    def uniquePaths_combination(self, m: int, n: int) -> int:
        def factorial(n):
            ans = 1
            for i in range(2,n+1):
                ans *= i
            return ans
        return factorial(m+n-2)//(factorial(n-1)*factorial(m-1))