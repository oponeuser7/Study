def fib(n):
    dp = [0]*100
    dp[0], dp[1] = 0, 1
    for i in range(2, 100):
       dp[i] = dp[i-1]+dp[i-2]
    return dp[n]

def main():
    n = int(input())
    print(fib(n))

if __name__=="__main__": main()
