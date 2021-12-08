def lcs(a, b):
    dp = [[0]*(len(b)+1) for _ in range(len(a)+1)]
    for i in range(len(a)+1):
        for j in range(len(b)+1):
            if i==0 or j==0:
                dp[i][j] = 0
            elif a[i-1]==b[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    return dp[i][j] 

def main():
    a = input()
    b = input()
    print(lcs(a,b))

if __name__=="__main__": main()

