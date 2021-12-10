class Solution:
    #Title: Domino and Tromino Tiling
    #Approach: DP
    #Explanation: First you have to define the subproblem. In this problem,
    #subproblem would be count of ways to tile 2xn board. We are going to
    #define this answer f(n). First, we can find that f(n) consists of f(n-1)
    #and f(n-2) since it is same as adding 2x1 block to f(n-1) and adding two
    #1x2 blocks to f(n-2). But what about the others? You can think of image
    #that 2xn block with tromino block on it's nth index. In this situation,
    #there is no connection between this block and previous results. Which mean
    #s this would be a new way to tile 2xn board and so on and on.
    def numTilings(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0], dp[1], dp[2] = 1, 1, 2
        for i in range(3, n+1):
            temp = dp[i-1] + dp[i-2]
            for j in range(i-3, -1, -1):
                temp += 2*dp[j]
            dp[i] = temp
        return dp[n]%1000000007
