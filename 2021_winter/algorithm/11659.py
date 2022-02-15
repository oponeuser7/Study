import sys

def solve(n, m, p):
    return p[m]-p[n-1]

def main():
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    p = [0]*(n+1)
    p[0] = 0
    temp = 0
    for i in range(n):
        temp += nums[i]
        p[i+1] = temp
    for i in range(m):
        i, j = map(int, sys.stdin.readline().split())
        print(solve(i, j, p))

if __name__=="__main__": main()
