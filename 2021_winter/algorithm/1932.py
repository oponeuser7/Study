def solve(n, t):
    dp = [[0 for i in range(n)] for j in range(n)]
    print(dp)
    for i in range(n):
        dp[-1][i] = t[-1][i]
    for i in range(n-2, -1, -1):
        for j in range(i+1):
            dp[i][j] = t[i][j] + max(dp[i+1][j], dp[i+1][j+1])
    return dp[0][0]
            
def main():
    n = int(input())
    t = [[] for i in range(n)]
    for i in range(n):
        t[i] = list(map(int, input().split()))
    print(t)
    print(solve(n, t))

if __name__=="__main__": main()
